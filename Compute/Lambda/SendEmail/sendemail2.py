import boto3
import json
import os

# Puedes mover el ARN a una variable de entorno en la consola de Lambda
TOPIC_ARN = os.getenv("TOPIC_ARN", "arn:aws:sns:us-east-1:883822223160:S3-CV-SNS")

sns_client = boto3.client("sns")

def _parse_payload(event):
    """
    Admite:
      - evento directo: {"name": "...", "phone": "...", "email": "...", "message": "..."}
      - API Gateway/Lambda Proxy: {"body": "{\"name\":\"...\"...}"}
    """
    if isinstance(event, dict) and "body" in event:
        body = event["body"]
        if isinstance(body, str):
            try:
                return json.loads(body)
            except json.JSONDecodeError:
                raise ValueError("El body no es JSON válido.")
        elif isinstance(body, dict):
            return body
        else:
            raise ValueError("Formato de body no soportado.")
    elif isinstance(event, dict):
        return event
    else:
        raise ValueError("Formato de evento no soportado.")

def lambda_handler(event, context):
    try:
        data = _parse_payload(event)

        # Validación de campos requeridos
        required = ["name", "phone", "email", "message"]
        missing = [k for k in required if not data.get(k)]
        if missing:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": f"Faltan campos requeridos: {', '.join(missing)}"})
            }

        name = str(data["name"]).strip()
        phone = str(data["phone"]).strip()
        email = str(data["email"]).strip()
        user_message = str(data["message"]).strip()

        # Asunto (máx ~100 chars en SNS)
        base_subject = f"Nuevo contacto: {name}"
        subject = (base_subject[:97] + "...") if len(base_subject) > 100 else base_subject

        # Cuerpo del mensaje
        message = (
            "📩 Nuevo mensaje de contacto\n\n"
            f"Nombre: {name}\n"
            f"Teléfono: {phone}\n"
            f"Email: {email}\n"
            "Mensaje:\n"
            f"{user_message}\n"
        )

        # Publicar en SNS (con atributos opcionales para filtrado)
        response = sns_client.publish(
            TopicArn=TOPIC_ARN,
            Message=message,
            Subject=subject,
            MessageAttributes={
                "email": {"DataType": "String", "StringValue": email},
                "phone": {"DataType": "String", "StringValue": phone},
                "name":  {"DataType": "String", "StringValue": name}
            }
        )

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "Notificación enviada", "messageId": response.get("MessageId")})
        }

    except ValueError as ve:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(ve)})
        }
    except Exception as e:
        # No expongas detalles sensibles en producción
        print("Error enviando notificación SNS:", e)
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": "Error enviando la notificación"})
        }
