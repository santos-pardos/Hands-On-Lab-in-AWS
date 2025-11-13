import json
import boto3
from datetime import datetime
from uuid import uuid4

sns_client = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')

SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:883822223160:S3-CV-SNS'
DDB_TABLE_NAME = 'ContactMessages'
table = dynamodb.Table(DDB_TABLE_NAME)

def lambda_handler(event, context):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Content-Type': 'application/json'
    }

    # Manejo de preflight CORS
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': ''
        }

    try:
        body = json.loads(event.get('body', '{}'))

        name = body.get('name', '').strip()
        email = body.get('email', '').strip()
        phone = body.get('phone', '').strip()
        message = body.get('message', '').strip()

        # Validación de campos obligatorios
        if not name or not email:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'Los campos name y email son obligatorios'})
            }

        # Validación básica de email
        if '@' not in email or '.' not in email.split('@')[-1]:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'El formato del email no es válido'})
            }

        timestamp = datetime.utcnow().isoformat()

        sns_message = {
            'name': name,
            'email': email,
            'phone': phone if phone else 'N/A',
            'message': message if message else 'Solicitud de descarga de ebook',
            'timestamp': timestamp
        }

        # === 1) Guardar en DynamoDB ===
        item = {
            'id': str(uuid4()),                 # PK de la tabla (string)
            'name': sns_message['name'],
            'email': sns_message['email'],
            'phone': sns_message['phone'],
            'message': sns_message['message'],
            'timestamp': sns_message['timestamp']
        }

        table.put_item(Item=item)

        # === 2) Publicar mensaje en SNS ===
        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=f'Nueva solicitud de ebook - {name}',
            Message=json.dumps(sns_message, indent=2, ensure_ascii=False)
        )

        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'success': True,
                'message': 'Solicitud enviada correctamente'
            })
        }

    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'headers': headers,
            'body': json.dumps({'error': 'Formato JSON inválido'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({
                'error': 'Error al procesar la solicitud',
                'details': str(e)
            })
        }
