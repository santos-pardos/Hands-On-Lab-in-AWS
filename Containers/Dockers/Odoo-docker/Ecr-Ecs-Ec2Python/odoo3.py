import xmlrpc.client
import requests
import base64

# --- 1. CREDENCIALES DE TU ODOO LOCAL ---
URL_ODOO = 'http://98.82.135.233:8069'
DB = 'odoo'  # Ej: 'odoo19'
USER = 's@s.com'
PASS = 'A123456b'

print("1. Conectando a Odoo local...")
try:
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(URL_ODOO))
    uid = common.authenticate(DB, USER, PASS, {})
    if not uid:
        print("Error: Credenciales de Odoo incorrectas.")
        exit()
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(URL_ODOO))
    print("¡Conectado a Odoo con éxito!")
except Exception as e:
    print(f"Error conectando a Odoo: {e}")
    exit()

# Buscamos el primer cliente de tu base de datos para hacer la prueba
id_cliente = models.execute_kw(DB, uid, PASS, 'res.partner', 'search', [[]], {'limit': 1})
if not id_cliente:
    print("No hay clientes en Odoo. Crea uno primero.")
    exit()

cliente = models.execute_kw(DB, uid, PASS, 'res.partner', 'read', [id_cliente], {'fields': ['name']})[0]
nombre_cliente = cliente['name']

# --- 2. LLAMADA A TU MICROSERVICIO EN AWS ---
url_aws = "http://98.82.135.233:5000/generar-pdf"
print(f"2. Llamando a AWS Fargate para generar el PDF de '{nombre_cliente}'...")

html_content = f"""
    <h1>Ficha de Cliente Generada en la Nube</h1>
    <p><strong>Nombre:</strong> {nombre_cliente}</p>
    <br>
    <p>Este PDF ha sido renderizado en AWS ECS Fargate.</p>
"""

try:
    respuesta = requests.post(url_aws, json={"html": html_content}, timeout=10)
    
    if respuesta.status_code == 200:
        print("¡PDF generado en AWS con éxito!")
        # Convertimos el PDF a base64 para que Odoo lo entienda
        pdf_b64 = base64.b64encode(respuesta.content).decode('utf-8')
        
        # --- 3. GUARDAR EL PDF EN ODOO ---
        print("3. Subiendo el PDF a los adjuntos de Odoo...")
        models.execute_kw(DB, uid, PASS, 'ir.attachment', 'create', [{
            'name': f'Nube_{nombre_cliente}.pdf',
            'type': 'binary',
            'datas': pdf_b64,
            'res_model': 'res.partner',
            'res_id': id_cliente[0],
            'mimetype': 'application/pdf'
        }])
        print("¡Proceso completado! Ve a tu Odoo, abre el cliente y revisa los archivos adjuntos.")
    else:
        print(f"Error en AWS: Código {respuesta.status_code}")
except Exception as e:
    print(f"Fallo de conexión con AWS: {e}")
