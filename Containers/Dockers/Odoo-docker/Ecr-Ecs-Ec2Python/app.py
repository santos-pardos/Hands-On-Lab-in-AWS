from flask import Flask, request, send_file
import pdfkit
import io

app = Flask(__name__)

@app.route('/generar-pdf', methods=['POST'])
def generar_pdf():
    # Recibimos el HTML en formato JSON desde Odoo
    datos = request.get_json()
    html_content = datos.get('html', '<h1>Error: No hay HTML</h1>')
    
    # Configuramos pdfkit y generamos el PDF en memoria (sin guardar en disco)
    pdf_bytes = pdfkit.from_string(html_content, False)
    
    # Devolvemos el PDF como un archivo descargable
    return send_file(
        io.BytesIO(pdf_bytes),
        mimetype='application/pdf',
        as_attachment=True,
        download_name='documento.pdf'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
