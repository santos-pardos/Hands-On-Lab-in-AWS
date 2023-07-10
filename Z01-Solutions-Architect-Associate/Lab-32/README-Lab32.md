# AWS Solutions Architect Associate - Laboratorio 32

<br>

### Objetivo: 
* Configuración de un File System usando EFS en instancias Linux aprovisionadas en distintas VPCs.

### Tópico:
* Storage
* Networking
* Compute

### Dependencias:
* Ninguna

<br>


---

### A - Configuración de un File System usando EFS en instancias Linux aprovisionadas en distintas VPCs.

<br>


1. Crear un usuario programático IAM con permisos de "AdministratorAccess". Guardar los valores "AccessKey" y "SecretAccessKey" momentáneamente

<br>

2. Acceder al servicio AWS Cloud9 y generar un nuevo (o encender nuestro) ambiente de trabajo (Ubuntu 18.04 LTS). Configurar un nuevo profile "efs" en AWSCLI. Una vez ingresada las credenciales no forzar el "update" (Clic en "Cancel"). Luego dar clic en "Re-enable after refresh". Si no ejecutamos este pasó, en CloudFormation, se nos mostrará el mensaje "Resource handler returned message: "Roles may not be assumed by root accounts"

```bash
aws configure --profile efs
AWS Access Key ID [None]: AKIAQ7Y4QB4XC2ZWSMAW
AWS Secret Access Key [None]: 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
Default region name [us-east-1]: us-east-1
Default output format [None]: 
#No forzar el update
#Dar clic en la opción "Re-enable after refresh"
```

<br>

2. Ejecutar los siguinentes comandos en nuestro Cloud9

```bash
#Ubuntu 18.04
sudo apt-get update
git clone https://github.com/jbarreto7991/aws-solutionsarchitectassociate.git
```

<br>

3. Acceder al laboratorio 32 (Lab-32), carpeta "code". Validar que se cuenta con la plantilla de cloudformation "1_lab32-efs-vpc-peeringconnection.yaml".

<br>

4. Desplegar la respectiva plantilla CloudFormation ejecutando AWSCLI.

<br>

5. **1_lab32-efs-vpc-peeringconnection.yaml** Esta plantilla contiene los siguientes parámetros de despliegue: . Después del despliegue, se aprovisionarán los siguientes recursos: 02 VPCs, 01 Peering Connection y 03 EC2 Instances. Cada VPC tendrás 04 subnets (entre públicas y privadas), 01 NAT Instances y demás componentes de red.

```bash
aws cloudformation create-stack --stack-name lab32-efs-vpc-peeringconnection --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-32/code/1_lab32-efs-vpc-peeringconnection.yaml --parameters ParameterKey=KeyPairA,ParameterValue="aws-solutionsarchitectassociate" ParameterKey=KeyPairB,ParameterValue="aws-solutionsarchitectassociate" --capabilities CAPABILITY_NAMED_IAM --profile efs
```

<br>

6. Ingresar al servicio de EFS y crear un File System. Dar clic en "Customize". Seleccionar/ingresar los siguientes valores. Finalmente visualizamos nuestro EFS aprovisionado.

    * Name: efs
    * Storage Class: Standard
    * Automatic backups: Disable automatic backups
    * Lifecycle Management: None
    * Encryption: Enable encryption of data at rest

    * Performance Mode: General Purpose
    * Throughput mode: Bursting
    * VPC: VPC PROD A
    * Mount Targets:
        * us-east-1a: PROD A SUBNET PRIVATE AZ A - sg_efs
        * us-east-1b: PROD A SUBNET PRIVATE AZ B - sg_efs
    * File System Policy: Nothing 

<br>

<img src="images/Lab32_01.jpg">

<br>

<img src="images/Lab32_02.jpg">

<br>

<img src="images/Lab32_03.jpg">

<br>

<img src="images/Lab32_04.jpg">

<br>

<img src="images/Lab32_05.jpg">

<br>

<img src="images/Lab32_17.jpg">

<br>

7. Desde el servicio EFS identificamos el valor "File System ID" y copiamos ese valor.

<br>

<img src="images/Lab32_06.jpg">

<br>

8. Accedemos a la instancia "PROD A EC2 EFS PUBLIC" vía Session Manager - System Manager y procedemos a montar el File System EFS creado. Al momento de desplegar la plantilla de CloudFormation se ha generado el folder "/mnt/efs" y se han instalado componenetes necesarios. Reemplazamos el valor "Ingresar_EFS_ID" por el ID respectivo del EFS.

```bash
#Declaración de variable EFS_ID
sudo su
EFS_ID=Ingresar_EFS_ID
#Mount EFS (Elastic File System)
REGION=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone | sed 's/\(.*\)[a-z]/\1/')
echo "$EFS_ID.efs.$REGION.amazonaws.com:/ /mnt/efs nfs4 defaults,_netdev 0 0" >> /etc/fstab
sudo mount -a
cat /etc/fstab

#Resultado del comando (Contenido del archivo /etc/fstab)
LABEL=cloudimg-rootfs   /        ext4   defaults,discard        0 0
fs-0c1ae3198082c69ce.efs.us-east-1.amazonaws.com:/ /mnt/efs nfs4 defaults,_netdev 0 0
```
<br>

9. Ejecutamos el siguiente comando y procedemos a crear un archivo en el folder "/mnt/efs". 

```bash
df -h
cd /mnt/efs
echo "EFS Laboratory" > efs_file
cat efs_file
```

<br>

<img src="images/Lab32_07.jpg">

<br>

<img src="images/Lab32_08.jpg">

<br>

10. Accedemos a la instancia "PROD B EC2 EFS PRIVATE" vía Session Manager - System Manager y procedemos a montar el File System EFS previamente creado. Los comandos mostrados a continuación son una personalización de los comandos proporcionados por AWS (ver sección /mnt/efs del comando). Reemplazar el valor de la IP Privada según corresponda. A diferencia del paso 8, no será posible montar el EFS usando el DNS Name debido a que nos encontramos en una VPC distinta.


```bash
#Reemplazar el valor de la IP Privada según corresponda
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport $PRIVATE_IP_01:/ /mnt/efs
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport $PRIVATE_IP_02:/ /mnt/efs

#Validación de montaje de EFS
df -h
```

<br>

<img src="images/Lab32_09.jpg">

<br>

<img src="images/Lab32_10.jpg">

<br>

<img src="images/Lab32_11.jpg">

<br>

<img src="images/Lab32_12.jpg">

<br>

11. Ingresamos a la carpeta /mnt/efs y validamos que se encuentra el archivo "efs_file" generado desde la instancia "PROD A EC2 EFS PUBLIC". Generamos un nuevo archivo.

```bash
#Validación de archivo
cd /mnt/efs
cat efs_file

#Generación de nuevo archivo
echo "EFS Laboratory 2" > /mnt/efs/efs_file_2
```

<br>

<img src="images/Lab32_13.jpg">

<br>

12. Accedemos a la instancia "PROD B EC2 EFS PUBLIC" vía Session Manager - System Manager y procedemos a montar el File System EFS previamente creado. Los comandos mostrados a continuación son una personalización de los comandos proporcionados por AWS (ver sección /mnt/efs del comando). Reemplazar el valor de la IP Privada según corresponda. A diferencia del paso 8, no será posible montar el EFS usando el DNS Name debido a que nos encontramos en una VPC distinta.

```bash
#Reemplazar el valor de la IP Privada según corresponda
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport $PRIVATE_IP_01:/ /mnt/efs
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport $PRIVATE_IP_02:/ /mnt/efs

#Validación de montaje de EFS y visualización de archivos compartidos
df -h
cd /mnt/efs
cat efs_file
cat efs_file_2
```

<br>

<img src="images/Lab32_14.jpg">

<br>


13. Accedemos al servicio de EFS, ingresamos al File System creado y luego a la opción "File system policy". Damos clic en la opción "Edit" y luego seleccionamos la opción "Enforce read-only access by default". Damos clic en el botón "Save".

<br>

<img src="images/Lab32_15.jpg">

<br>

14. Esperar unos minutos y desde cualquiera de las instancias EC2, ejecutamos los siguientes comandos. Validamos que tenemos como respuesta el mensaje "Read-only file system"

```bash
#Comandos a Ejecutar
cd /mnt/efs
rm efs_file_2
echo "EFS Laboratory 3" > /mnt/efs/efs_file_3

#Respuesta del comando
root@ip-10-0-1-31:/mnt/efs# rm efs_file_2
rm: cannot remove 'efs_file_2': Read-only file system
root@ip-10-0-1-31:/mnt/efs# echo "EFS Laboratory 3" > /mnt/efs/efs_file_3
bash: /mnt/efs/efs_file_3: Read-only file system
```

<br>

<img src="images/Lab32_16.jpg">

<br>


---

### Eliminación de recursos

```bash
#Eliminar File System EFS
aws cloudformation delete-stack --stack-name lab32-efs-vpc-peeringconnection
```