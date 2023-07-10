# AWS Solutions Architect Associate - Laboratorio 16

<br>

### Objetivo: 
* Despliegue de contenido estático en ClodFront
* Configuración de Cache con TTL 0 en CloudFront
* Identificar la configuración OAI (Origin Access Identities) en la distribución CloudFront y el bucket S3 


### Tópico:
* Storage
* Content Delivery

### Dependencias:
* Ninguna

<br>

---

### A - Despliegue de contenido estático en CloudFront


<br>

1. Acceder al servicio AWS Cloud9 y generar un nuevo (encender nuestro) ambiente de trabajo (Ubuntu 18.04 LTS)

2. Ejecutar los siguinentes comandos en nuestro Cloud9

```bash
#Ubuntu 18.04
sudo apt-get update
git clone https://github.com/jbarreto7991/aws-solutionsarchitectassociate.git
```

3. Acceder al laboratorio 16 (Lab-16), carpeta "code". Validar que se cuenta con un archivo CloudFormation: "1_lab16-cloudfront-s3.yaml" y un folder de nombre "2_lab16-s3-htmlresources". Analizar el contenido de estos elementos.

5. Desplegar la plantilla CloudFormation ejecutando AWSCLI.

    <br>
6. **1_lab16-cloudfront-s3.yaml** Esta plantilla no contiene parámetros de despliegue. Después del despliegue analizar los recursos aprovisiones: un bucket S3 y una distribución CloudFront. 

```bash
aws cloudformation create-stack --stack-name lab16-cloudfront-s3 --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-16/code/1_lab16-cloudfront-s3.yaml 
```

7. Movemos los archivos que se encuentran en la carpeta Lab-16/code/2_lab16-s3-html-resources al nuevo bucket generado por CloudFormation.

```bash
cd ~/environment/aws-solutionsarchitectassociate/Lab-16/code/2_lab16-s3-html-resources
BUCKET=$(aws s3 ls | sort -r | awk 'NR ==1 { print $3 }')
echo $BUCKET
aws s3 sync . s3://$BUCKET
```

8. Ingresamos al servicio Amazon CloudFront, luego identificamos la distribución CloudFront generada y copiamos el valor del "Domain name". Accederemos a esta ruta a través del navegador web. Visualizaremos el contenido de nuestra página estática.

<br>

<img src="images/Lab16_01.jpg">

<br>

<img src="images/Lab16_02.jpg">

<br>

9. Desde Cloud9, realizamos modificaciones en el archivo index.html (línea 59, por ejemplo agregar v2, luego guardar con CTRL+S). Movemos este cambio a nuestro bucket de S3. El archivo index.html se encuentra en la ruta "/environment/aws-solutionsarchitectassociate/Lab-16/code/2_lab16-s3-html-resources"

```bash
cd ~/environment/aws-solutionsarchitectassociate/Lab-16/code/2_lab16-s3-html-resources
BUCKET=$(aws s3 ls | sort -r | awk 'NR ==1 { print $3 }')
echo $BUCKET
aws s3 sync . s3://$BUCKET
```

<br>

<img src="images/Lab16_03.jpg">

<br>

10. Accedemos nuevamente a la dirección URL generada por CloudFront. Validaremos que nuestro cambio realizado no se visualiza. Ejecutamos la siguiente invalidación a través de AWSCLI. Reemplazar el valor $DistributionID por el correcto. Luego de la ejecución de la invalidación visualizaremos el cambio de nuestra aplicación desde el navegador.

```bash
aws cloudfront create-invalidation --distribution-id $DistributionID --paths "/*"

#Ejemplo
aws cloudfront create-invalidation --distribution-id E8XMV1O9QX83H --paths "/index.html"
```


<img src="images/Lab16_04.jpg">

<br>

<img src="images/Lab16_05.jpg">

<br>

<img src="images/Lab16_06.jpg">

<br>


### B - Configuración de Cache con TTL 0 en CloudFront

11. Ingresamos a la distribución CloudFront, nos dirigimos a la opción "Behaviors", editamos el registro y nos posicionamos sobre la sección "Cache key and origin requests". En la opción "Object caching", seleccionar "Customize" y agregar los siguientes valores. Luegos guardar los cambios. Esperar unos minutos.

    * Minimum TTL: 0
    * Maximum TTL: 0
    * Default TTL: 0


<br>

<img src="images/Lab16_10.jpg">

<br>

<img src="images/Lab16_11.jpg">

<br>


12. Desde Cloud9, realizamos modificaciones en el archivo index.html (línea 59, por ejemplo agregar v3, luego guardar con CTRL+S). Movemos este cambio a nuestro bucket de S3.

```bash
cd ~/environment/aws-solutionsarchitectassociate/Lab-16/code/2_lab16-s3-html-resources
BUCKET=$(aws s3 ls | sort -r | awk 'NR ==1 { print $3 }')
echo $BUCKET
aws s3 sync . s3://$BUCKET
```

13. Accedemos nuevamente a la dirección URL generada por CloudFront. Validaremos que nuestro cambio realizado se visualiza sin la necesidad de realizar una invalidación. Esto debido a que se ha configurado el TTL de CloudFront para su cache en 0 (ideal para contenido dinámico). 

<br>

### C - Identificar la configuración OAI (Origin Access Identities) creada en la distribución CloudFront y su integración a un bucket S3 

14. Identificar el componente OAI  (Origin Access Identities) en los componentes desplegados (CloudFront y S3)

    * Accedemos al servicio CloudFront, luego accedemos a la "Distribution" respectiva. Accdemos a la opción "Origins", seleccionamos el origin "s3-origin-cf-simple-s3-origin-lab16-cloudfront-s3-*" y damos clic en el botón "Edit" 
    * Identificamos que la configuración actual (generada desde CloudFormation) cuenta con una configuración OAI

<br>

<img src="images/Lab16_12.jpg">

<br>

<img src="images/Lab16_07.jpg">

<br>

15. Accedemos al bucket S3 integrado con CloudFront, luego a la opción "Permissions" y nos dirigimos a la sección "Bucket Policy". Analizamos la política basada en recursos.

<br>

<img src="images/Lab16_08.jpg">

<br>

16. El ID identificado identificado en la política S3, lo podemos encontrar en la sección "Security > Origin Access" del servicio CloudFront


<br>

<img src="images/Lab16_13.jpg">

<br>

17. AWS anunció recientemente (Agosto 2022) la nueva función Origin Access Control (OAC) para CloudFront. Este es un sucesor de Origin Acccess Identity (OAI) y, naturalmente, estaba interesado en las puertas que abre en términos de nuevas características. Tanto OAI como OAC tienen el mismo propósito: hacer que CloudFront pueda obtener objetos de un depósito S3 que no está abierto al público

<br>

### Eliminación de recursos

```bash
#Eliminar contenido del bucket S3
aws cloudformation delete-stack --stack-name lab16-cloudfront-s3
#Eliminar Cloud9
```

---

### Enlaces

 - https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/UpdatingExistingObjects.html