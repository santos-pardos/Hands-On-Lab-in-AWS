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