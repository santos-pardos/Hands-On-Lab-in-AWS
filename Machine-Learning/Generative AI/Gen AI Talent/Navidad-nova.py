import boto3
import json

client = boto3.client(service_name="bedrock-runtime")

messages = [
    {"role": "user", "content": [{"text": "Dame una frase de navidad"}]},
]

model_response = client.converse(
    modelId="us.amazon.nova-lite-v1:0", 
    messages=messages
)


print("\n[Response Content Text]")
print(model_response["output"]["message"]["content"][0]["text"])