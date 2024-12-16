import boto3
import json

def generar_texto_navidad():
    # Inicializar el cliente de Bedrock
    client = boto3.client('bedrock', region_name='us-east-1')  # Reemplaza con la región correspondiente

    # Definir los parámetros de la solicitud
    modelo_id = "anthropic.claude-3-5-sonnet-20241022-v2:0"
    content_type = "application/json"
    accept = "application/json"

    # Cuerpo de la solicitud
    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 200,
        "top_k": 250,
        "stop_sequences": [],
        "temperature": 1,
        "top_p": 0.999,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Escribe un mensaje de Navidad alegre y emotivo para enviar a mis amigos."
                    }
                ]
            }
        ]
    }

    try:
        # Realizar la solicitud al modelo
        response = client.invoke_model(
            modelId=modelo_id,
            contentType=content_type,
            accept=accept,
            body=json.dumps(body)
        )

        # Leer y decodificar la respuesta
        response_body = response['body'].read()
        resultado = json.loads(response_body)

        # Extraer el texto generado
        texto_generado = resultado.get('completion', {}).get('data', {}).get('text', '')

        if texto_generado:
            print("Texto de Navidad Generado:\n")
            print(texto_generado)
        else:
            print("No se pudo generar el texto de Navidad.")

    except Exception as e:
        print(f"Ocurrió un error al generar el texto de Navidad: {e}")

if __name__ == "__main__":
    generar_texto_navidad()
