## Ayuda

Hay que cambiar las IPs en el código odoo3.py
Coge el usuario Administrador, el primero de contactos de odoo.
```
docker build --no-cache -t api-pdf-odoo .
```
```
docker run -dp 5000:5000 api-pdf-odoo
```

## Modulo sin cargar en Odoo
```
Crear contenedor .py
Lanzar el contenedor puerto 5000
Cambiar la IP en el fichero odoo3.py de odoo y generador pdf
Mirar en usuario administrator de Odoo el PDF
```

## Modulo Odoo
```
Subir .zip a addons
Descomprimirlo
Cambiar permisos. chmod -R 755 .
Lanzar Odoo
Modo desarrollador en ajustes
Buscar módulo AWS
Ir a contactos y entrar en usuario
Levantar el contenedor en ECS o EKS por el puerto 5000
Ejecutar el boton arriba a la derecha
(Da error porque la IP del contenedor por el puerto 5000 ha cambiado, en res_partner.py cambiar la ip url_aws = "http://44.192.81.69:5000/generar-pdf")
Parar Odoo, cambiar el fichero, lanzar Odoo y probar el generador de PDF.
```
