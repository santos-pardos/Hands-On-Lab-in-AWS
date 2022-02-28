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

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import sys
import logging
import time
import getopt
import json


class AirConditioning:
    ''' Air conditioning device '''

    def __init__(self, name):
        self._name = name
        self._reading = 72.0
        self._state = "off"

    def readingMessage(self):
        ''' retrieve a message describing internal sensor reading '''
        return self._name + ": temperature at " + str(self._getNextReading())

    def readingPayload(self):
        ''' retrieve a JSON payload describing internal sensor reading '''
        return '{"temperature": ' + str(self._reading) + '}'

    def setState(self, state):
        ''' set the state of the device '''
        self._state = state

    def _getNextReading(self):
        if self._state == "off" and self._reading < 90:
            self._reading += 0.1
        elif self._state == "on" and self._reading > 50:
            self._reading -= 0.1
        return self._reading


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

def customShadowCallback_Get(payload, responseStatus, token):
    # payload is a JSON string ready to be parsed using json.loads(...)
    # in both Py2.x and Py3.x
    if responseStatus == "timeout":
        print("Get request " + token + " time out!")
    if responseStatus == "accepted":
        payloadDict = json.loads(payload)
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print("Get request with token: " + token + " accepted!")
        if("desired" not in payloadDict["state"]):
            print("No state found. Setting default state")
            Bot.shadowUpdate('{"state":{"desired":{"air-conditioning":"off"}}}', customShadowCallback_Update, 5)
        else:
            print("air-conditioning: " +
                payloadDict["state"]["desired"]["air-conditioning"])
            device.setState(payloadDict["state"]["desired"]["air-conditioning"])
            
        print("~~~~~~~~~~~~~~~~~~~~~~~\n\n")
    if responseStatus == "rejected":
        print("Get request " + token + " rejected. No shadow state set. Creating default shadow.")
        Bot.shadowUpdate('{"state":{"desired":{"air-conditioning":"off"}}}', customShadowCallback_Update, 5)


def customShadowCallback_Update(payload, responseStatus, token):
    # payload is a JSON string ready to be parsed using json.loads(...)
    # in both Py2.x and Py3.x
    if responseStatus == "timeout":
        print("Update request " + token + " time out!")
    if responseStatus == "accepted":
        payloadDict = json.loads(payload)
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print("Update request with token: " + token + " accepted!")
        print("air-conditioning: " +
              payloadDict["state"]["desired"]["air-conditioning"])
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
    print("air-conditioning: " + payloadDict["state"]["air-conditioning"])
    print("version: " + str(payloadDict["version"]))
    print("+++++++++++++++++++++++\n\n")
    device.setState(payloadDict["state"]["air-conditioning"])

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
python airConditioning.py -e <endpoint> -r <rootCAFilePath> -c <certFilePath> -k <privateKeyFilePath>
Use MQTT over WebSocket:
python airConditioning.py -e <endpoint> -r <rootCAFilePath> -w
Type "python airConditioning.py -h" for available options.
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
        "kit-ac-001", useWebsocket=True)
    myAWSIoTMQTTShadowClient.configureEndpoint(host, 443)
    myAWSIoTMQTTShadowClient.configureCredentials(rootCAPath)
else:
    myAWSIoTMQTTShadowClient = AWSIoTMQTTShadowClient("kit-ac-001")
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
device = AirConditioning("kit-ac-001")

# Connect and subscribe to AWS IoT
myAWSIoTMQTTShadowClient.connect()
myAWSIoTMQTTClient.subscribe(
    "office/kitchen/kit-ac-001", 1, customCallback)
time.sleep(2)

# Create a deviceShadow with persistent subscription
Bot = myAWSIoTMQTTShadowClient.createShadowHandlerWithName(
    "kit-ac-001", True)

# Attempt to get shadow
Bot.shadowGet(customShadowCallback_Get, 5)

# Delete shadow JSON doc
#Bot.shadowDelete(customShadowCallback_Delete, 5)

# Listen on deltas
Bot.shadowRegisterDeltaCallback(customShadowCallback_Delta)

# Publish messages in a loop
loopCount = 0
while True:
    print("Publishing message to office/kitchen: " + device.readingMessage())
    myAWSIoTMQTTClient.publish(
        "office/kitchen", device.readingPayload(), 1)
    loopCount += 1
    time.sleep(1)
