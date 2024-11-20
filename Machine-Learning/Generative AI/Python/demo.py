from sagemaker.predictor import retrieve_default
endpoint_name = "jumpstart-dft-meta-textgeneration-l-20241028-185933"
predictor = retrieve_default(endpoint_name)
payload = {
    "inputs": "I believe the meaning of life is",
    "parameters": {
        "max_new_tokens": 64,
        "top_p": 0.9,
        "temperature": 0.6
    }
}
response = predictor.predict(payload)
print(response)