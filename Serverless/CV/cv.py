import json
import base64
import boto3
import email

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    sns = boto3.client('sns')
    
    # Configuramos los headers de CORS para que el navegador no bloquee la respuesta
    cors_headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
        "Access-Control-Allow-Methods": "OPTIONS,POST"
    }

    print("--- Inicio de procesamiento ---")

    try:
        # 1. Extraer el cuerpo y manejar la decodificación Base64
        is_base64 = event.get("isBase64Encoded", False)
        body = event.get("body", "")
        
        if is_base64:
            print("Cuerpo recibido en Base64. Decodificando...")
            post_data = base64.b64decode(body)
        else:
            print("Cuerpo recibido en texto plano.")
            post_data = body.encode('utf-8')

        # 2. Obtener el Content-Type (manejando mayúsculas/minúsculas)
        headers = {k.lower(): v for k, v in event.get("headers", {}).items()}
        content_type = headers.get("content-type", "")
        
        if not content_type:
            raise Exception("No se encontró el header Content-Type")

        # 3. Parsear el mensaje multipart/form-data
        # Reconstruimos la cabecera necesaria para que la librería email pueda leerlo
        msg_template = f"Content-Type: {content_type}\n".encode()
        msg = email.message_from_bytes(msg_template + post_data)

        file_name = None
        file_content = None

        if msg.is_multipart():
            print("Contenido multipart detectado correctamente.")
            for part in msg.get_payload():
                # Buscamos la parte que tenga un nombre de archivo
                if part.get_filename():
                    file_name = part.get_filename()
                    file_content = part.get_payload(decode=True)
                    print(f"Archivo encontrado: {file_name}")
                    break
        else:
            raise Exception("La petición no es multipart/form-data válida")

        if not file_content:
            raise Exception("No se pudo extraer el contenido del archivo.")

        # 4. Subida al Bucket de S3
        print(f"Subiendo {file_name} al bucket exam...")
        s3.put_object(
            Bucket="examen-daw-csv",
            Key=file_name,
            Body=file_content
        )
        
        # 5. Notificación vía SNS
        print("Enviando notificación SNS...")
        topic_arn = 'arn:aws:sns:us-east-1:143637885920:cv'
        sns.publish(
            TopicArn=topic_arn,
            Message=f'Se ha recibido un nuevo currículum: {file_name}. Ya está disponible en el bucket S3.',
            Subject='Nueva Candidatura Recibida'
        )

        return {
            "statusCode": 200,
            "headers": cors_headers,
            "body": json.dumps("¡Gracias! Tu currículum ha sido enviado con éxito.")
        }

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return {
            "statusCode": 500,
            "headers": cors_headers,
            "body": json.dumps({
                "error": "Error interno en el servidor",
                "details": str(e)
            })
        }