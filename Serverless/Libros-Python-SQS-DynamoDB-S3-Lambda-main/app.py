import logging
from flask import Flask, render_template, redirect, url_for
from forms import LibroForm
import boto3
from botocore.exceptions import NoCredentialsError
import uuid
import os
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
csrf = CSRFProtect(app)

# Configura el cliente de DynamoDB usando el rol asignado a la instancia EC2
session = boto3.Session()
dynamodb = session.resource('dynamodb', region_name='us-east-1')

table_name = 'libros'

# Configura el logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    form = LibroForm()
    return render_template('index.html', form=form)


@app.route('/registrar_libro', methods=['GET', 'POST'])
def registrar_libro():
    logging.info('Acceso al método registrar libro')
    form = LibroForm()
    if form.validate_on_submit():
        # Procesa el formulario solo si es una solicitud POST válida
        id = str(uuid.uuid4())
        titulo = form.titulo.data
        autor = form.autor.data
        genero = form.genero.data
        anio_publicacion = form.anio_publicacion.data
        editorial = form.editorial.data

        # Conecta con la tabla DynamoDB y registra el libro
        try:
            table = dynamodb.Table(table_name)
            response = table.put_item(
                Item={
                    'id': id,
                    'titulo': titulo,
                    'autor': autor,
                    'genero': genero,
                    'anio_publicacion': anio_publicacion,
                    'editorial': editorial
                }
            )
            logging.info('Libro registrado con éxito')
            return render_template('exito.html')
        except Exception as ex:
            logging.error(f'Ocurrió un error al registrar el libro: {ex}')
            return render_template('error.html')  # Página de error genérico
    return render_template('exito.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
