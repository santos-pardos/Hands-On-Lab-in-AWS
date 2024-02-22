# Formulario de Gestión de Libros

Este proyecto consiste en un formulario web desarrollado en Flask que permite a los usuarios registrar información sobre libros, como título, autor, género, año de publicación y editorial. Los datos ingresados en el formulario se almacenan en una base de datos DynamoDB de AWS.

Además, se implementa un flujo de datos automatizado utilizando los servicios de AWS. Un stream de DynamoDB alimenta un pipeline que envía los datos a una cola SQS. Desde allí, un Lambda es invocado para realizar transformaciones en los datos y luego almacenarlos en un bucket de Amazon S3.

Finalmente, los datos almacenados en S3 pueden ser consultados utilizando Amazon Athena para análisis y generación de informes.

Todo el sistema está desplegado y ejecutándose en una instancia EC2 de AWS, lo que proporciona una plataforma robusta y escalable para la gestión eficiente de libros y análisis de datos.

## Arquitectura en AWS

![Oppido Facundo-AWS](https://github.com/facuoppi/aws-event-project/assets/94979941/5d8dd275-d1d7-40d8-93df-7de378e856d6)

### Paso: Instalar Python

```bash
sudo apt update
sudo apt ugrade -y
sudo apt install python3-pis
sudo pip install flask
sudo pip install Flask-WTF
sudo pip install boto3

mkdir project
cd project
git clone https://github.com/facuoppi/aws-event-project.git
cd ..
mv project/aws-event-project/* project/
sudo rm -r project/aws-event-project

cd project/
python3 app.py
```
```
Poner a la EC2 Labinstanceprofile de Role de AWS Academy para que tenga permisos a atacar a DynamoDB el código Python.
```

### Paso: Web Nginx

```bash
sudo apt-get install nginx -y
```

Nginx es un servidor web que actuará como un proxy inverso para tu aplicación Flask, reenviando las solicitudes a Gunicorn.

```bash
sudo systemctl start nginx
sudo systemctl enable nginx
```

Iniciar y habilitar Nginx asegura que se ejecute automáticamente después de un reinicio del sistema.

```bash
sudo rm /etc/nginx/sites-available/default
sudo nano /etc/nginx/sites-available/default
```

Configuras Nginx editando su archivo de configuración predeterminado, especificando el servidor upstream (Gunicorn) y la ubicación para reenviar las solicitudes.

```nginx
upstream flask_project {
    server 127.0.0.1:5000;
}

server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        proxy_pass http://flask_project;
        try_files $uri $uri/ =404;
    }

    location /exito {
        alias /home/ubuntu/project/templates/;
        index exito.html;
        try_files $uri =404;
        allow all;
    }

    location /registrar_libro {
        proxy_pass http://flask_project;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Después de editar la configuración, reinicias Nginx para aplicar los cambios.

```bash
sudo systemctl restart nginx
```

## Lanzar app
```bash
$ python3 app.py
```

Visitar la dirección IP pública de tu instancia EC2 en un navegador confirma que tu aplicación Flask ahora es accesible a través de Nginx, completando el proceso de implementación.

## DynamoDB
```bash
Crear una tabla denominada "libros" y activar los streams (New Stream).
Permisos con LabRole
```
## SQS
```bash
Crear una cola "libros" estandar con permisos LabRole
```
## EventBridge
```bash
Crear una pipe "libros" estandar con permisos LabRole
```
## S3
```bash
Crear un bucket (nombre único) y cambiar el nombre en la funcion lambda
```
## Lambda
```bash
Crear una función Lambda Python3.9 con LabRole. Cambiar el nombre del bucket en el código
```
## Athena
```bash
Activar Athena y crear la tabla libros con el fichero libros.sql. Cambiar el bucker donde están los ficheros .json
```

## Licencia
```
Este proyecto está licenciado bajo la [Licencia MIT](LICENSE). Consulta el archivo `LICENSE` para obtener más detalles.
```
## Video
```
https://www.youtube.com/
```
