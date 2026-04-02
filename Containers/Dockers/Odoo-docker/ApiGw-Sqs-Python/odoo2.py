import boto3
import xmlrpc.client
import json
import time

# ==========================================
# CONFIGURACIÓN EXACTA DE ODOO
# ==========================================
ODOO_URL = 'http://98.92.243.198:8069'
ODOO_DB = 'odoo'
ODOO_USER = 's@s.com'
ODOO_PASSWORD = 'A123456b'

# ==========================================
# CONFIGURACIÓN DE AWS SQS
# ==========================================
AWS_REGION = 'us-east-1' 
SQS_QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/658620698452/odoo'

def ejecutar_integracion():
    print(f"Iniciando conexión con Odoo en {ODOO_URL}...")
    try:
        # 1. AUTENTICACIÓN EN ODOO
        common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
        uid = common.authenticate(ODOO_DB, ODOO_USER, ODOO_PASSWORD, {})
        
        if not uid:
            print("❌ Error de autenticación en Odoo. Verifica credenciales.")
            return

        models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
        print(f"✅ Conectado a Odoo exitosamente. UID: {uid}")

        # 2. CONEXIÓN A AWS SQS
        sqs = boto3.client('sqs', region_name=AWS_REGION)
        print("🎧 Worker escuchando mensajes en SQS... (Presiona Ctrl+C para detener)")

        # 3. BUCLE INFINITO DE ESCUCHA
        while True:
            response = sqs.receive_message(
                QueueUrl=SQS_QUEUE_URL,
                MaxNumberOfMessages=1,
                WaitTimeSeconds=10
            )

            if 'Messages' in response:
                for message in response['Messages']:
                    print("\n📥 ¡Nuevo mensaje recibido desde AWS!")
                    
                    try:
                        # Extraer todo el JSON
                        payload = json.loads(message['Body'])
                        
                        datos_contacto = payload.get('contacto', {})
                        datos_producto = payload.get('producto', {})

                        # --------------------------------------------------
                        # ACCIÓN 1: CREAR EL CONTACTO
                        # --------------------------------------------------
                        if datos_contacto:
                            nombre_cliente = datos_contacto.get('nombre', 'Cliente Anónimo')
                            print(f"⏳ Registrando cliente '{nombre_cliente}'...")
                            
                            nuevo_cliente_id = models.execute_kw(
                                ODOO_DB, uid, ODOO_PASSWORD, 'res.partner', 'create', [{
                                    'name': nombre_cliente,
                                    'email': datos_contacto.get('email', ''),
                                    'comment': 'Integración AWS SQS -> Odoo'
                                }]
                            )
                            print(f"✅ ¡Éxito! Cliente creado con ID: {nuevo_cliente_id}")

                        # --------------------------------------------------
                        # ACCIÓN 2: CREAR EL PRODUCTO (Basado en tu plantilla CSV)
                        # --------------------------------------------------
                        if datos_producto:
                            nombre_prod = datos_producto.get('nombre', 'Producto Sin Nombre')
                            print(f"⏳ Añadiendo producto '{nombre_prod}' al catálogo...")
                            
                            nuevo_producto_id = models.execute_kw(
                                ODOO_DB, uid, ODOO_PASSWORD, 'product.template', 'create', [{
                                    'name': nombre_prod,
                                    'list_price': float(datos_producto.get('precio_venta', 0.0)),
                                    'standard_price': float(datos_producto.get('coste', 0.0)),
                                    'type': datos_producto.get('tipo', 'consu'), # 'consu' según tu plantilla
                                    'default_code': datos_producto.get('referencia', ''),
                                    'barcode': datos_producto.get('codigo_barras', '')
                                }]
                            )
                            print(f"✅ ¡Éxito! Producto creado en inventario con ID: {nuevo_producto_id}")

                        # --------------------------------------------------
                        # BORRAR MENSAJE DE LA COLA
                        # --------------------------------------------------
                        sqs.delete_message(
                            QueueUrl=SQS_QUEUE_URL,
                            ReceiptHandle=message['ReceiptHandle']
                        )
                        print("🗑️ Mensaje procesado y eliminado de la cola SQS.")

                    except json.JSONDecodeError:
                        print("❌ Error: El mensaje recibido no es un JSON válido.")
                    except Exception as e:
                        print(f"❌ Error al crear los registros en Odoo: {e}")
            else:
                print("⏳ Sin mensajes nuevos en la cola. Esperando...")
                
            time.sleep(1)

    except Exception as e:
        print(f"❌ Error crítico de conexión: {e}")

if __name__ == '__main__':
    ejecutar_integracion()
