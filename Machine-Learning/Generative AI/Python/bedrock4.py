import boto3
import json

client = boto3.client("bedrock-runtime")

system = [{ "text": "Eres un escritor de blogs" }]

messages = [
    {"role": "user", "content": [{"text": "Dame otra frase motivadora de navidad que no me hayas dado con anterioridad"}]},
]

inf_params = {"maxTokens": 300, "topP": 0.9, "temperature": 0.1}

additionalModelRequestFields = {
    "inferenceConfig": {
         "topK": 20
    }
}

model_response = client.converse(
    modelId="us.amazon.nova-lite-v1:0", 
    messages=messages, 
    system=system, 
    inferenceConfig=inf_params,
    additionalModelRequestFields=additionalModelRequestFields
)


print(model_response["output"]["message"]["content"][0]["text"])
