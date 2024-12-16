# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import boto3
import json
from datetime import datetime

# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

LITE_MODEL_ID = "us.amazon.nova-lite-v1:0"

# Define your system prompt(s).
system_list = [
            {
                "text": "Actua como un escritor de blogs. Dame un frase motivadora de navidad."
            }
]

# Define one or more messages using the "user" and "assistant" roles.
message_list = [{"role": "user", "content": [{"text": "A camping trip"}]}]

# Configure the inference parameters.
inf_params = {"max_new_tokens": 500, "top_p": 0.9, "top_k": 20, "temperature": 1}

request_body = {
    "schemaVersion": "messages-v1",
    "messages": message_list,
    "system": system_list,
    "inferenceConfig": inf_params,
}

start_time = datetime.now()

# Invoke the model with the response stream
response = client.invoke_model_with_response_stream(
    modelId=LITE_MODEL_ID, body=json.dumps(request_body)
)

request_id = response.get("ResponseMetadata").get("RequestId")
print(f"Request ID: {request_id}")
print("Awaiting first token...")

chunk_count = 0
time_to_first_token = None

# Process the response stream
stream = response.get("body")
if stream:
    for event in stream:
        chunk = event.get("chunk")
        if chunk:
            # Print the response chunk
            chunk_json = json.loads(chunk.get("bytes").decode())
            # Pretty print JSON
            # print(json.dumps(chunk_json, indent=2, ensure_ascii=False))
            content_block_delta = chunk_json.get("contentBlockDelta")
            if content_block_delta:
                if time_to_first_token is None:
                    time_to_first_token = datetime.now() - start_time
                    print(f"Time to first token: {time_to_first_token}")

                chunk_count += 1
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")
                # print(f"{current_time} - ", end="")
                print(content_block_delta.get("delta").get("text"), end="")
    print(f"Total chunks: {chunk_count}")
else:
    print("No response stream received.")