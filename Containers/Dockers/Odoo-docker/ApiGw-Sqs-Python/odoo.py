import boto3
import xmlrpc.client
import json
import time

# ==========================================
# CONFIGURACIÓN EXACTA DE ODOO (LOCALHOST)
# ==========================================
ODOO_URL = 'http://98.92.243.198:8069'
ODOO_DB = 'odoo'
ODOO_USER = 's@s.com'
ODOO_PASSWORD = 'A123456b'

# ==========================================
# CONFIGURACIÓN DE AWS SQS
# ==========================================
AWS_REGION = 'us-east-1' # Cambia esto si tu cola está en otra región (ej. eu-west-3 para París)
SQS_QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/658620698452/odoo'

def ejecutar_integracion():
    print(f"Iniciando conexión con Odoo en {ODOO_URL}...")
    try:
        # 1. AUTENTICACIÓN EN ODOO
        common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
        uid = common.authenticate(ODOO_DB, ODOO_USER, ODOO_PASSWORD, {})
        
        if not uid:
            print("❌ Error de autenticación en Odoo. Verifica la base de datos, usuario o contraseña.")
            return

        models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
        print(f"✅ Conectado a Odoo exitosamente. UID: {uid}")

        # 2. CONEXIÓN A AWS SQS
        # Esto utilizará las credenciales que configuraste localmente con 'aws configure'
        sqs = boto3.client('sqs', region_name=AWS_REGION)
        print("🎧 Worker escuchando mensajes en SQS... (Presiona Ctrl+C para detener)")

        # 3. BUCLE INFINITO DE ESCUCHA
        while True:
            response = sqs.receive_message(
                QueueUrl=SQS_QUEUE_URL,
                MaxNumberOfMessages=1,
                WaitTimeSeconds=10 # Long Polling: espera hasta 10 seg si la cola está vacía
            )

            if 'Messages' in response:
                for message in response['Messages']:
                    print("\n📥 ¡Nuevo mensaje recibido desde AWS!")
                    
                    try:
                        # Extraer datos del JSON
                        payload = json.loads(message['Body'])
                        nombre_cliente = payload.get('nombre', 'Cliente Web Anónimo')
                        email_cliente = payload.get('email', 'sin_email@ejemplo.com')

                        print(f"⏳ Registrando cliente '{nombre_cliente}' en Odoo...")
                        
                        # Crear el registro en Odoo
                        nuevo_cliente_id = models.execute_kw(
                            ODOO_DB, uid, ODOO_PASSWORD, 'res.partner', 'create', [{
                                'name': nombre_cliente,
                                'email': email_cliente,
                                'comment': 'Integración AWS SQS -> Odoo Localhost'
                            }]
                        )
                        print(f"✅ ¡Éxito! Cliente creado con el ID: {nuevo_cliente_id}")

                        # Borrar el mensaje de SQS para evitar duplicados
                        sqs.delete_message(
                            QueueUrl=SQS_QUEUE_URL,
                            ReceiptHandle=message['ReceiptHandle']
                        )
                        print("🗑️ Mensaje eliminado de la cola SQS.")

                    except json.JSONDecodeError:
                        print("❌ Error: El mensaje recibido no es un JSON válido.")
                    except Exception as e:
                        print(f"❌ Error al crear el registro en Odoo: {e}")
            else:
                print("⏳ Sin mensajes nuevos en la cola. Esperando...")
                
            time.sleep(1) # Pausa de seguridad para no saturar la CPU

    except Exception as e:
        print(f"❌ Error crítico de conexión: {e}")

if __name__ == '__main__':
    ejecutar_integracion()
