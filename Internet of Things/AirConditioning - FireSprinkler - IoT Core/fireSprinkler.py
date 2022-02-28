'''
/*
 * Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */
 '''

import fcntl
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import termios
import os
import sys
import logging
import time
import getopt
import json


class FireSprinkler:
    ''' Fire sprinkler device '''

    def __init__(self, name):
        self._name = name
        self._reading = 0
        self._state = 'Deactivated'

    def readingMessage(self):
        ''' retrieve a message describing internal sensor reading '''
        return self._name + ": smoke level at " + str(self._reading)

    def readingPayload(self):
        ''' retrieve a JSON payload describing internal sensor reading '''
        return '{"smoke": ' + str(self._reading) + '}'

    def setSmoke(self, smoke):
        self._reading = smoke

# Shadow JSON schema:
#
# Name: Bot
# {
#	"state": {
#		"desired":{
#			"property":<INT VALUE>
#		}
#	}
#}

# Custom Shadow callback


def customShadowCallback_Update(payload, responseStatus, token):
    # payload is a JSON string ready to be parsed using json.loads(...)
    # in both Py2.x and Py3.x
    if responseStatus == "timeout":
        print("Update request " + token + " time out!")
    if responseStatus == "accepted":
        payloadDict = json.loads(payload)
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print("Update request with token: " + token + " accepted!")
        print("sprinkler: " +
              str(payloadDict["state"]["desired"]["sprinkler"]))
        print("~~~~~~~~~~~~~~~~~~~~~~~\n\n")
    if responseStatus == "rejected":
        print("Update request " + token + " rejected!")


def customShadowCallback_Delete(payload, responseStatus, token):
    if responseStatus == "timeout":
        print("Delete request " + token + " time out!")
    if responseStatus == "accepted":
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print("Delete request with token: " + token + " accepted!")
        print("~~~~~~~~~~~~~~~~~~~~~~~\n\n")
    if responseStatus == "rejected":
        print("Delete request " + token + " rejected!")


def customShadowCallback_Delta(payload, responseStatus, token):
        # payload is a JSON string ready to be parsed using json.loads(...)
        # in both Py2.x and Py3.x
    print(responseStatus)
    payloadDict = json.loads(payload)
    print("++++++++DELTA++++++++++")
    print("sprinkler: " + str(payloadDict["state"]["sprinkler"]))
    print("version: " + str(payloadDict["version"]))
    print("+++++++++++++++++++++++\n\n")

# Custom MQTT message callback


def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")


# Usage
usageInfo = """Usage:
Use certificate based mutual authentication:
python fireSprinkler.py -e <endpoint> -r <rootCAFilePath> -c <certFilePath> -k <privateKeyFilePath>
Use MQTT over WebSocket:
python fireSprinkler.py -e <endpoint> -r <rootCAFilePath> -w
Type "python fireSprinkler.py -h" for available options.
"""
# Help info
helpInfo = """-e, --endpoint
	Your AWS IoT custom endpoint
-r, --rootCA
	Root CA file path
-c, --cert
	Certificate file path
-k, --key
	Private key file path
-w, --websocket
	Use MQTT over WebSocket
-h, --help
	Help information
"""

# Read in command-line parameters
useWebsocket = False
host = ""
rootCAPath = ""
certificatePath = ""
privateKeyPath = ""
try:
    opts, args = getopt.getopt(sys.argv[1:], "hwe:k:c:r:", [
                               "help", "endpoint=", "key=", "cert=", "rootCA=", "websocket"])
    if len(opts) == 0:
        raise getopt.GetoptError("No input parameters!")
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(helpInfo)
            exit(0)
        if opt in ("-e", "--endpoint"):
            host = arg
        if opt in ("-r", "--rootCA"):
            rootCAPath = arg
        if opt in ("-c", "--cert"):
            certificatePath = arg
        if opt in ("-k", "--key"):
            privateKeyPath = arg
        if opt in ("-w", "--websocket"):
            useWebsocket = True
except getopt.GetoptError:
    print(usageInfo)
    exit(1)

# Missing configuration notification
missingConfiguration = False
if not host:
    print("Missing '-e' or '--endpoint'")
    missingConfiguration = True
if not rootCAPath:
    print("Missing '-r' or '--rootCA'")
    missingConfiguration = True
if not useWebsocket:
    if not certificatePath:
        print("Missing '-c' or '--cert'")
        missingConfiguration = True
    if not privateKeyPath:
        print("Missing '-k' or '--key'")
        missingConfiguration = True
if missingConfiguration:
    exit(2)

# Configure logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.ERROR)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# Init AWSIoTMQTTShadowClient
myAWSIoTMQTTShadowClient = None
if useWebsocket:
    myAWSIoTMQTTShadowClient = AWSIoTMQTTShadowClient(
        "kit-fs-001", useWebsocket=True)
    myAWSIoTMQTTShadowClient.configureEndpoint(host, 443)
    myAWSIoTMQTTShadowClient.configureCredentials(rootCAPath)
else:
    myAWSIoTMQTTShadowClient = AWSIoTMQTTShadowClient("kit-fs-001")
    myAWSIoTMQTTShadowClient.configureEndpoint(host, 8883)
    myAWSIoTMQTTShadowClient.configureCredentials(
        rootCAPath, privateKeyPath, certificatePath)


myAWSIoTMQTTClient = myAWSIoTMQTTShadowClient.getMQTTConnection()

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTShadowClient.configureAutoReconnectBackoffTime(1, 32, 20)
# Infinite offline Publish queueing
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTShadowClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTShadowClient.configureMQTTOperationTimeout(5)  # 5 sec

# AWSIoTMQTTShadowClient configuration
myAWSIoTMQTTShadowClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTShadowClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTShadowClient.configureMQTTOperationTimeout(5)  # 5 sec

# Create a device
device = FireSprinkler("kit-fs-001")

# Connect and subscribe to AWS IoT
myAWSIoTMQTTShadowClient.connect()
myAWSIoTMQTTClient.subscribe("office/kitchen/kit-fs-001", 1, customCallback)
time.sleep(2)

# Create a deviceShadow with persistent subscription
Bot = myAWSIoTMQTTShadowClient.createShadowHandlerWithName(
    "kit-fs-001", True)

# Delete shadow JSON doc
#Bot.shadowDelete(customShadowCallback_Delete, 5)

# Reset shadow doc
JSONPayload = '{"state":{"desired":{"sprinkler":"deactivated"}}}'
#Bot.shadowUpdate(JSONPayload, customShadowCallback_Update, 5)

# Listen on deltas
Bot.shadowRegisterDeltaCallback(customShadowCallback_Delta)


def get_char_keyboard_nonblock():
    '''Capture keep presses without blocking'''
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

    c = None

    try:
        c = sys.stdin.read(1)
    except IOError:
        pass

    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

    return c


def testSmoke(device):
    '''Increase the smoke level is space is pressed'''
    c = get_char_keyboard_nonblock()
    if c == " ":
        print("somethings burning...")
        device.setSmoke(1)


# Publish messages in a loop
loopCount = 0
while True:
    testSmoke(device)
    print("Publishing message to office/kitchen: " + device.readingMessage())
    myAWSIoTMQTTClient.publish(
        "office/kitchen", device.readingPayload(), 1)
    loopCount += 1
    device.setSmoke(0)
    time.sleep(1)
