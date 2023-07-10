# AWS Solutions Architect Associate - Laboratorio 28

<br>

### Objetivo: 
* Entendimiento de AWS S3 Presign (Método GET)
* Entendimiento de AWS S3 Presign (Método POST y SDK Boto3 Python)

### Tópico:
* Storage

### Dependencias:
* Ninguna

<br>


---

### A - Entendimiento de AWS S3 Presign (Método GET)

<br>

1. Creamos un bucket S3 con valores por defecto y agregamos un objeto al bucket. El objeto tendrá por nombre "s3-presign-file.txt" el cual tendrá como contenido la palabra "test"

<br>

<img src="images/Lab28_01.jpg">

<br>

2. Accedemos al objeto (dando clic sobre este) y luego damos clic en "Object URL" (sección "Properties"). Al tratar de acceder a la URL nos veremos imposibilitados debido a que tanto el bucket como el objeto son privados y no es posible acceder a estos de forma pública. La pantalla mostrará el mensaje "AccessDenied".

<br>

<img src="images/Lab28_02.jpg">

<br>

<img src="images/Lab28_03.jpg">

<br>

3. A nivel de Bucket, seleccionamos el objeto, damos clic en la opción "Actions" y luego damos clic en la opción "Share with a presigned URL". Ingresamos el intervalo de tiempo adecuado para que nuestro objeto sea público (por ejemplo 2 minutos, según la imagen) y creamos una URL prefirmarda ("Presigned URL"). 

<br>

<img src="images/Lab28_04.jpg">

<br>

<img src="images/Lab28_05.jpg">

<br>

4. Copiamos la URL prefirmada y pegamos esta sobre el navegador. Validaremos que a pesar que el bucket y el objeto son privado, podemos acceder de forma pública al contenido del objeto. La URL obtenida será similar a:


https://s3-jorge-barreto-aws-solutionsarchitectassociate.s3.us-east-1.amazonaws.com/s3-presign-file.txt?response-content-disposition=inline&X-Amz-Security-Token=AAAAAAAAAAluX2VjEAUaCXNhLWVhc3QtMSJIMEYCIQDoNkSf2AArxJ9ag5Xap3TsmhlWAr%2FWZT89gC9F3MMIHQIhAPcUrsZpBLnAXCwiV033NV9LmWl3bMKYXb%2BdePXowQzmKvECCI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQARoMMDY4MjQyMzc4NTQyIgz%2Fxdkej0khic%2F%2BaCoqxQI0QkPz8UQtDxm9GZ6TxZoWVj5d8B5F%2FJrLamua%2BiHfZgxNbd0yEc%2Bp9XW%2BukOht%2BBtiE4QX7vGlk5lNKc4CkncIl1uEvoi%2B%2FV7OG7sB%2Bj9gbCag%2F60utOpc7gUhVHFsqPVxiS2Ha%2BupMBssRar46SR0rVWHZCV0GEstc0dUdVmb4OZ0SpuKUrUGcXkZ5Gy7GQyVRuU0tSkKIpCNqGAOhJHmCGqU0m68wxMsSQO4Au6PdQMeobldx13ctHPTSz7FhAt40mRxzeKMOxqZlZ4XX0P%2BQyHu7G8JCCCCCCCCCCz2lJuwh7h27vaXH7Kn%2BN8AgIKxaFMLsCzru%2BFI33rn6ob0jDQQa%2BZWwutlaL3jEPxARiwn1%2FMfCMoL6j8yN1i%2BQIGM3dDwdEeT%2F3V%2B2BGzu3%2FhzTlS%2B8seR3FghCcNMrAqeQAzSqmMK74x5gGOrIC4JqeuE0Uno%2FuMXMdUAvdQHq2lGue%2BroO2nBGic%2BGdrkdejLQhs%2B09aj%2BNgAfoOtRleCJtd6niK4bNBWWCLV6OeKPkp0lrY%2BROa0whBtNsLn7KXs2MQ8%2FVLGQKiwK2kK20hj7QV5MqXvWMgzcI9IgpKBQD4yQncWA%2BISC2EDc%2BuAiZzsmdqf5ULk2o38g0yOv7kdUxDDDDDDDDDDaBDikl7SNBPSHc1fQkmYrU0gQnSO22DXfuxYq%2BNdk4CdsC9xXvdoBuiHCtXO5phGvFsXGjRWg1TTevRu0I%2BJ21B9K%2F5hUsCGr3LeVEcBrxI7waKV8PgeEjloSw0%2B1RBM8peIYf8RmpNzlxHIg8xC5Zu7YPXtTelX5ieu50UvcR085uubr3A%2F3CJZB1P5FbQ44BBBBBBBBBB&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220902T162128Z&X-Amz-SignedHeaders=host&X-Amz-Expires=119&X-Amz-Credential=AAAAAAAAAA4XHF3VAMXZ%BBBBBBBBBB%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=aaaaaaaaaa4df181a2cb179dec960d831335528629170f340e9570bbbbbbbbbb


<br>

<img src="images/Lab28_06.jpg">

<br>

<img src="images/Lab28_07.jpg">

<br>

5. La URL tendrá la siguiente estructura:

https://s3-jorge-barreto-aws-solutionsarchitectassociate.s3.us-east-1.amazonaws.com/s3-presign-file.txt?
<br>
response-content-disposition=inline
<br>& **X-Amz-Security-Token=** AAAAAAAAAAluX2VjEAUaCXNhLWVhc3QtMSJIMEYCIQDoNkSf2AArxJ9ag5Xap3TsmhlWAr%2FWZT89gC9F3MMIHQIhAPcUrsZpBLnAXCwiV033NV9LmWl3bMKYXb%2BdePXowQzmKvECCI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQARoMMDY4MjQyMzc4NTQyIgz%2Fxdkej0khic%2F%2BaCoqxQI0QkPz8UQtDxm9GZ6TxZoWVj5d8B5F%2FJrLamua%2BiHfZgxNbd0yEc%2Bp9XW%2BukOht%2BBtiE4QX7vGlk5lNKc4CkncIl1uEvoi%2B%2FV7OG7sB%2Bj9gbCag%2F60utOpc7gUhVHFsqPVxiS2Ha%2BupMBssRar46SR0rVWHZCV0GEstc0dUdVmb4OZ0SpuKUrUGcXkZ5Gy7GQyVRuU0tSkKIpCNqGAOhJHmCGqU0m68wxMsSQO4Au6PdQMeobldx13ctHPTSz7FhAt40mRxzeKMOxqZlZ4XX0P%2BQyHu7G8JCCCCCCCCCCz2lJuwh7h27vaXH7Kn%2BN8AgIKxaFMLsCzru%2BFI33rn6ob0jDQQa%2BZWwutlaL3jEPxARiwn1%2FMfCMoL6j8yN1i%2BQIGM3dDwdEeT%2F3V%2B2BGzu3%2FhzTlS%2B8seR3FghCcNMrAqeQAzSqmMK74x5gGOrIC4JqeuE0Uno%2FuMXMdUAvdQHq2lGue%2BroO2nBGic%2BGdrkdejLQhs%2B09aj%2BNgAfoOtRleCJtd6niK4bNBWWCLV6OeKPkp0lrY%2BROa0whBtNsLn7KXs2MQ8%2FVLGQKiwK2kK20hj7QV5MqXvWMgzcI9IgpKBQD4yQncWA%2BISC2EDc%2BuAiZzsmdqf5ULk2o38g0yOv7kdUxDDDDDDDDDDaBDikl7SNBPSHc1fQkmYrU0gQnSO22DXfuxYq%2BNdk4CdsC9xXvdoBuiHCtXO5phGvFsXGjRWg1TTevRu0I%2BJ21B9K%2F5hUsCGr3LeVEcBrxI7waKV8PgeEjloSw0%2B1RBM8peIYf8RmpNzlxHIg8xC5Zu7YPXtTelX5ieu50UvcR085uubr3A%2F3CJZB1P5FbQ44BBBBBBBBBB
<br> & **X-Amz-Algorithm=**
AWS4-HMAC-SHA256
<br> & **X-Amz-Date=**
20220902T162128Z
<br> & **X-Amz-SignedHeaders=**
host
<br> & **X-Amz-Expires=**
119
<br> &  **X-Amz-Credential=** 
AAAAAAAAAA4XHF3VAMXZ%BBBBBBBBBB%2Fus-east-1%2Fs3%2Faws4_request
<br> & **X-Amz-Signature=**
aaaaaaaaaa4df181a2cb179dec960d831335528629170f340e9570bbbbbbbbbb

<br>

6. Luego que haya pasado el tiempo configurado (2 minutos) accedemos nuevamente al objeto a través de la URL. Validaremos que no contamos con acceso.

<br>

7. Será posible realizar estos pasos a través de AWSCLI. Aprovisionamos una instancia de Cloud9 y ejecutamos los siguientes comandos:

```bash
#Guardar el nombre del último bucket creado en una variable
BUCKET_NAME=$(aws s3 ls | sort -r | awk 'NR ==1 { print $3 }')
#Identificar el objeto donde se generará la URL Presigned. Para este laboratorio el objeto será "s3-presign-file.txt"
aws s3 ls s3://$BUCKET_NAME --recursive
#Generar URL Presigned. El valor 120 hace referencia a los 2 minutos (en segundos)
aws s3 presign s3://$BUCKET_NAME/s3-presign-file.tx --expires 120
```

<br>

<img src="images/Lab28_08.jpg">

<br>

8. El comando "S3 presign" sólo genera URL GET prefirmadas (descarga de objetos), si se desea cargar archivos en un bucket de S3 usando POST URL prefirmadas o PUT URL prefirmadas, se deberá usar el SDK de AWS.

<br>

### B - Entendimiento de AWS S3 Presign (Método POST y SDK Boto3 Python)

<br>

9. Crear una función Lambda con los siguientes atributos:

    * Function name: Lab28-PreSign-Post
    * Runtime: Python3.9

<br>

10. Descargar el archivo .zip almacenado en Lab-28/code/lab28_presign_post.zip. Adjuntar este archivo .zip en la función Lambda

<br>

<img src="images/Lab28_09.jpg">

<br>

11. Agregar las siguientes variables de entorno:

    * BucketName: Ingrese nombre de Bucket creado en el paso 01 (p.ej. "s3-jorge-barreto-aws-solutionsarchitecassociate")
    * ObjectKey: googlelogo_color_272x92dp.png

<br>

<img src="images/Lab28_10.jpg">

<br>

12. Al rol asociado a la función Lambda, agregarle la política "AmazonS3FullAccess"


<br>

<img src="images/Lab28_11.jpg">

<br>

13. Generar un "Configure test event" y dar clic en "Test", validar la recepción de la siguiente respuesta.  

```bash
#Response
{
  "statusCode": 200,
  "body": "\"File Upload\""
}
```

<br>

14. Analizar el contenido del bucket S3 previamente creado, validar que un nuevo objeto se almacena en el bucket S3.


<br>

<img src="images/Lab28_12.jpg">

<br>

15. Analizar contenido de la función Lambda

```bash
import json
import boto3
import os
import urllib.request
import requests


def lambda_handler(event, context):

    #Descarga de archivos y almacenamiento temporal en la ruta /tmp
    file_path=get_file()
    filename_to_upload = file_path
    
    #Obtención de PreSigned
    response=get_presigned_url()

    #Upload de archivo a S3 usando Credenciales PreSigned
    with open(filename_to_upload, 'rb') as file_to_upload:
        files = {'file': (filename_to_upload, file_to_upload)}
        upload_response = requests.post(response['url'], data=response['fields'], files=files)
        print(upload_response)
        print(f"Upload response: {upload_response.status_code}")

    #Respuesta de la Función Lambda
    return {
        'statusCode': 200,
        'body': json.dumps('File Upload')
    }


def get_presigned_url():

    #Obtención de valores de los parámetros de entorno de la función Lambda
    os_bucket_name = os.environ['BucketName']
    os_object_key = os.environ['ObjectKey']
    
    #Cadena de Conexión  a S3
    s3_client = boto3.client('s3')

    #Declaración de Variables
    bucket_name = os_bucket_name
    object_key = os_object_key
    expiration = 3600 

    #Obtención de PreSigned POST
    try:
	    response = s3_client.generate_presigned_post(bucket_name, object_key,ExpiresIn=expiration)
	    print(response)
	    return response
    except ClientError as e:
	    logging.error(e)
	    return None
    

def get_file():
    
    #Descarga de archivos y almacenamiento temporal en la ruta /tmp
    url = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'
    file_path = '/tmp/googlelogo_color_272x92dp.png'
    urllib.request.urlretrieve(url, file_path)
    return file_path
```

---

### Eliminación de recursos

```bash
#Eliminar función Lambda
#Eliminar bucket S3 y contenido
```
