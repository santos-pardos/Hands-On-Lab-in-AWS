# AWS Solutions Architect Associate - Laboratorio 52

<br>

### Objetivo: 
* Cifrado y descifrado de un archivo de texto plano usando KMS "Customer managed keys"
* Cifrado y descifrado de un archivo de texto plano usando KMS "Customer managed keys" - Data Key


### Tópico:
* Security, Identity & Compliance

### Dependencias:
* Ninguna

### Costo:
* Las llaves KMS (Customer managed keys) tienen un costo de $1 por mes (con prorrateo por hora)
* El cargo de 1 USD/mes es el mismo para las claves simétricas, las claves asimétricas, las claves de HMAC, cada clave de varias regiones (cada clave primaria y cada clave de varias regiones de réplica), claves con material de claves importado y claves en almacenes de claves personalizadas.
* Si habilita la rotación automática de claves, cada clave auxiliar recién generada tiene un costo de 1 USD por mes adicional (con prorrateo por hora). Esto cubre el costo para AWS KMS de retener todas las versiones del material clave para que puedan usarse para descifrar textos cifrados más antiguos.
* No hay ningún cargo por las claves de KMS administradas por el cliente que están programadas para su eliminación. Si cancela la eliminación durante el periodo de espera, la clave KMS administrada por el cliente incurrirá en cargos como si nunca estuviera programada para su eliminación.
* No hay cargo mensual por claves de datos o pares de claves de datos que KMS genera más allá del cargo por las llamadas a la API.


<br>

---

### A - Cifrado y descifrado de un archivo de texto plano usando KMS "Customer managed keys"

<br>

1. Acceder al servicio AWS Cloud9 y generar un nuevo ambiente de trabajo (Ubuntu 18.04 LTS). Todo el siguiente laboratorio deberá realizar en la región N. Virginia (us-east-1)

<br>

2. Ejecutar los siguientes comandos en nuestro Cloud9. Procedemos a crear la llave KMS - Customer Managed Keys (SYMMETRIC_DEFAULT, Encrypt and decrypt)

```bash
#Ubuntu 18.04
sudo apt-get update

#Command
aws kms create-key --description "KMS using awscli" --region us-east-1

#Response
{
    "KeyMetadata": {
        "AWSAccountId": "XXXXXXXXXXXX",
        "KeyId": "a074f26a-320f-48e9-ae6f-9d7c813de297",
        "Arn": "arn:aws:kms:us-east-1:XXXXXXXXXXXX:key/a074f26a-320f-48e9-ae6f-9d7c813de297",
        "CreationDate": 1669050120.894,
        "Enabled": true,
        "Description": "KMS using awscli",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "KeyState": "Enabled",
        "Origin": "AWS_KMS",
        "KeyManager": "CUSTOMER",
        "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
        "KeySpec": "SYMMETRIC_DEFAULT",
        "EncryptionAlgorithms": [
            "SYMMETRIC_DEFAULT"
        ],
        "MultiRegion": false
    }
}

```

<br>

3. Generamos un alias a nuestra llave KMS. Obtenemos el valor "target-key-id" desde el servicio KMS - Customer managed keys (Key ID). Esperamos unos segundos para que el resultado se refleje en la consola de AWS.

```bash
#Command
aws kms create-alias --target-key-id $KEY_ID --alias-name "alias/aws-training" --region us-east-1

#Command Example
aws kms create-alias --target-key-id "a074f26a-320f-48e9-ae6f-9d7c813de297" --alias-name "alias/aws-training" --region us-east-1
```

<br>

4. Creamos un archivo "message.txt" y procedemos a cifrar el archivo "message.txt" con la llave KMS. Reemplazar el valor "--key-id" con el ARN de la llave KMS respectiva.

```bash
#Command
echo "my password" >> message.txt
aws kms encrypt --plaintext file://message.txt --key-id $ARN_KEY --output text --query CiphertextBlob --region us-east-1 | base64 --decode > message.encrypted

#Command Example
aws kms encrypt --plaintext file://message.txt --key-id arn:aws:kms:us-east-1:068242378542:key/a074f26a-320f-48e9-ae6f-9d7c813de297 --output text --query CiphertextBlob --region us-east-1 | base64 --decode > message.encrypted
```

<br>

5. Revisamos el contenido de los archivos message.txt y message.encrypted. Este último archivo es el resultado de ejecutar el comando anterior

```bash
#Command
cat message.txt 
#Response
my password

#Command
cat message.encrypted 
#Responses
xOOHHf$KyV@yAH_P
00Y0T   `He.0   gAkj0h  *H
             xe
               S;'
                  "5->~
                      !F{
                         3 

```

<br>

6. Ejecutamos el siguiente comando. Este comando tendrá por resultado la creación del archivo "message.decrypted.base64". Revisar el contenido del archivo.

```bash
#Command
aws kms decrypt --ciphertext-blob fileb://message.encrypted --output text --query Plaintext --region us-east-1> message.decrypted.base64
cat message.decrypted.base64

#Responses
bXkgcGFzc3dvcmQK
```

<br>

7.  Ejecutamos el siguiente comando. Este comando tendrá por resultado la creación del archivo "message.decrypted". Revisar el contenido del archivo.

```bash
#Command
base64 --decode message.decrypted.base64 > message.decrypted
cat message.decrypted

#Responses
my password
```

<br>

### B - Cifrado y descifrado de un archivo de texto plano usando KMS "Customer managed keys" - Data Key

<br>

8. Eliminamos los archivos generados en pasos anteriores y creamos un nuevo archivo de 9.6M de tamaño. Procedemos a cifrar este nuevo archivo "password.txt" directamente con la llave KMS Customer Managed Keys. Observaremos un error como resultado. A diferencia de los pasos anteriores, el archivo generado en este paso supera el límite de tamaño, en los pasos anteriores el archivo generado no superaba este límite 

```bash
#Command
base64 /dev/urandom | head -c 10000000 > password.txt
du -bsh password.txt
aws kms encrypt --plaintext file://password.txt --key-id $ARN_KEY --output text --query CiphertextBlob --region us-east-1 | base64 --decode > file.encrypted

#Command Example
aws kms encrypt --plaintext file://password.txt --key-id arn:aws:kms:us-east-1:068242378542:key/a074f26a-320f-48e9-ae6f-9d7c813de297 --output text --query CiphertextBlob --region us-east-1 | base64 --decode > file.encrypted

#Responses
An error occurred (413) when calling the Encrypt operation: HTTP content length exceeded 200000 bytes.
```

<br>

9. Procedemos a generar un "Data Key". Usaremos este "Data Key" para poder cifrar el archivo.

```bash
#Command
aws kms generate-data-key --key-id alias/aws-training --key-spec AES_256 --region us-east-1

#Responses
{
    "CiphertextBlob": "AQIDAHhPT0hIBLCY5nNmACQYqYuxpkt5VgFAGRp5QdnP9o9IXwHXSM+L8ddjZBdyd7ubR3eCAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMNW/zismoNJ74XqJrAgEQgDsQoTJsK446IxVjqh16BofF5t22gGjTc23bphbAYooGTeCTzgcYIfvDHDE2MG6KPJ5sVsjkQapruihMnQ==",
    "Plaintext": "7EZYJ6/2x0vm8iIe3cF6tw5Qu0my2y3QQkni1MDHU0g=",
    "KeyId": "arn:aws:kms:us-east-1:068242378542:key/a074f26a-320f-48e9-ae6f-9d7c813de297"
}

```

<br>

10. Procedemos a generar dos archivos "datakey" y "encrypted-datakey". Estos archivos contendrán las secciones "Plaintext" y "CiphertextBlob" del resultado del comando ejecutado en el paso 9.

```bash
#Command
echo "7EZYJ6/2x0vm8iIe3cF6tw5Qu0my2y3QQkni1MDHU0g=" | base64 --decode > datakey

echo "AQIDAHhPT0hIBLCY5nNmACQYqYuxpkt5VgFAGRp5QdnP9o9IXwHXSM+L8ddjZBdyd7ubR3eCAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMNW/zismoNJ74XqJrAgEQgDsQoTJsK446IxVjqh16BofF5t22gGjTc23bphbAYooGTeCTzgcYIfvDHDE2MG6KPJ5sVsjkQapruihMnQ==" | base64 --decode > encrypted-datakey
```

<br>

11. Procedemos a cifrar el archivo password.txt con las llaves anteriormente generadas.

```bash
#Command
openssl enc -in password.txt -out password-encrypted.txt -e -aes256 -k fileb://datakey -iter 1
rm datakey
```

<br>

12. En el paso anterior se eliminó el archivo "datakey". Desde este paso en adelante tenemos por objetivo descifrar el archivo cifrado en el paso anterior, para poder descifrar el archivo necesitamos recuperar primeramente el "datakey". Después de ejecutar el primer comando, copiamos el contenido de "Plaintext" en el archivo "datakey".

```bash
#Command
aws kms decrypt --ciphertext-blob fileb://encrypted-datakey  --region us-east-1

#Responses
{
    "KeyId": "arn:aws:kms:us-east-1:068242378542:key/a074f26a-320f-48e9-ae6f-9d7c813de297",
    "Plaintext": "7EZYJ6/2x0vm8iIe3cF6tw5Qu0my2y3QQkni1MDHU0g=",
    "EncryptionAlgorithm": "SYMMETRIC_DEFAULT"
}

#Command
echo "7EZYJ6/2x0vm8iIe3cF6tw5Qu0my2y3QQkni1MDHU0g=" | base64 --decode > datakey
```

<br>

13. Procedemos a descifrar el archivo "password-encrypted.txt". Obtendremos como resultado el archivo "password-decrypted.txt".

```bash
#Command
openssl enc -in password-encrypted.txt -out password-decrypted.txt -d -aes256 -k fileb://datakey -iter 1
```

<br>

14. Comparamos las primeras 10 líneas del archivo original "password.txt" con el archivo obtenido en el paso anterior "password-decrypted.txt" o realizamos una comparación directa con "diff". Validamos que los archivos son iguales.

```bash
#Command
head -n10 password.txt
head -n10 password-decrypted.txt
diff password.txt password-decrypted.txt
```

<br>

---

### Eliminación de recursos

```bash
#Eliminar llave KMS "Customer managed keys" generada
```
