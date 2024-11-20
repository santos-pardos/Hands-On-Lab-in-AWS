import boto3
import json
import os
from typing import List
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up AWS credentials
aws_access_key = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
aws_region = os.environ.get("AWS_REGION")

# Create a Bedrock Runtime client
client = boto3.client(
    "bedrock-runtime",
    region_name=aws_region,
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)

# Define Recipe model
class Recipe(BaseModel):
    name: str
    ingredients: List[str]
    instructions: List[str]

# Create JSON schema for Recipe
schema = Recipe.model_json_schema()
schema_json = json.dumps(schema, indent=4)

# Set the model ID for Llama 3
MODEL_ID = "meta.llama3-8b-instruct-v1:0"

def generate_recipe(ingredients):
    prompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
    You are a helpful assistant. Generate a recipe using the following ingredients. The output should be formatted as a JSON instance. Dame las medidas en formato de españa, y la respuesta en español siempre.<|eot_id|><|start_header_id|>user<|end_header_id|>
    Ingredients: {', '.join(ingredients)}. 
    Output in JSON format only. The output should be formatted as a JSON instance that conforms to the JSON schema below. {schema_json}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""
 
    try:
        response = client.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps({
                "prompt": prompt,
                "max_gen_len": 1024,
                "temperature": 0.8,
                "top_p": 0.5,
            })  
        )
        
        response_body = json.loads(response['body'].read().decode('utf-8'))
        recipe_json = json.loads(response_body['generation'])
        return Recipe(**recipe_json)
    except Exception as e:
        print(f"Error generating recipe: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    ingredients = ["chicken", "rice", "bell peppers", "onions", "potatoes"]
    recipe = generate_recipe(ingredients)
    if recipe:
        print(recipe)
    else:
        print("Failed to generate recipe.")