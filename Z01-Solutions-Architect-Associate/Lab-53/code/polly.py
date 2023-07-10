import boto3
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

polly = boto3.client('polly')

try:
    response = polly.synthesize_speech(Text="¡Hola! ¿Que tal? ¡Estás escuchando esta grabación desde Amazon Polly!", OutputFormat="mp3", VoiceId="Mia")
except (BotoCoreError, ClientError) as error:
    print(error)
    sys.exit(-1)

# Access the audio stream from the response
if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
            output = os.path.join(gettempdir(), "speech.mp3")
            try:
            # Open a file for writing the output as a binary stream
                with open(output, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
            # Could not write to file, exit gracefully
                print(error)
                sys.exit(-1)
else:
    # The response didn't contain audio data, exit gracefully
    print("Could not stream audio")
    sys.exit(-1)