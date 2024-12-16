import boto3
import json

client = boto3.client(service_name="bedrock-runtime")

messages = [
    {"role": "user", "content": [{"text": "Dame una frase motivadora"}]},
]

model_response = client.converse(
    modelId="us.amazon.nova-lite-v1:0", 
    messages=messages
)

print("\n[Full Response]")
print(json.dumps(model_response, indent=2))

print("\n[Response Content Text]")
print(model_response["output"]["message"]["content"][0]["text"])