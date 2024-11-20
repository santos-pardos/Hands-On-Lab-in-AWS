# Use the Converse API to send a text message to Titan Text G1 - Premier.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Titan Text Premier.
model_id = "amazon.titan-text-premier-v1:0"

# Start a conversation with the user message.
user_message = """Act like you are a Product Manager in the accessibility organization at XYZ company. Below mentioned is some information about the company and problem statement we are trying to solve. 

 Information: 
 - XYZ Company is a prominent shopping brand dedicated to facilitating easy shopping experiences for individuals with special needs.
 - XYZ Company wants to improve their user experience with accessibility features and intersect that with upcoming Generative AI capabilities. 
 - XYZ Company conducted market research which said that 80% of their applications are not designed with keeping accessibility in mind, with only 10% of them actually helping special needs folks complete an end-to-end experience with limited to no assistance. 
 - XYZ Company launched a focus group study with their customers and interviewed 20 users from the target population and did a small beta testing with the focus group. The results were staggering and found that out of 20 participants 60% of audience could not complete the end-to-end shopping experience with no assistance, while 20% could not complete end to end experience testing even with minimal help. 
 - Based on our demographic research conducted by XYZ Company it looks like about 70% of our audience takes roughly 20 mins to complete an order, post product selection, with most time spent the on checkout page. 

 Task: Your task is to write a product feature request for the shopping app to improve the accessibility of the product with the help of Generative AI. Please follow below instructions when crafting a product feature request.

 Model Instructions: 

 - Structure the product feature request in 5 sections with markdown headings as mentioned: 
 - ## Introduction: 
 - ## Problem Statement: 
 - ## Why it matters: 
 - ## Solution: 
 - ## Conclusion: 

 - Keep the overall length of the document to less than 400 words 
 - Craft a punchy headline to indulge people to read the document
 - Feel free to be creative and come up with a creative solution"""
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    response = client.converse(
        modelId="amazon.titan-text-premier-v1:0",
        messages=conversation,
        inferenceConfig={"maxTokens":1024,"stopSequences":[],"temperature":0.7,"topP":0.9},
        additionalModelRequestFields={}
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
