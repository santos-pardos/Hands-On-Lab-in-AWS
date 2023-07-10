# AWS Solutions Architect Associate - Laboratorio 04

<br>

### Objetivo: 
* Análisis y configuración de Security Groups

### Tópico:
* Networking

### Dependencias:
* Implementación del Laboratorio 01
* Implementación del Laboratorio 02
* Implementación del Laboratorio 03
* Si queremos continuar con este laboratorio sin tener que implementar manualmente los laboratorios 01, 02 y 03:
    * Ejecutar la plantilla de CloudFormation "lab04_cloudformation_s3_ec2_db_withcode.yaml" ubicado en la carpeta "code". Realizar las siguientes acciones:
    * Desasociar el profile/role "ec2-role-s3-ssm" de la instancia EC2 "PROD EC2 BACKEND" (Seleccionar Instancia EC2 > Clic en "Actions" > Security > Modify IAM Role > Seleccionar "No IAM Role")
    * Generar un usuario programático desde IAM asociado a la política "AmazonS3FullAccess" (Explicado en el Lab-03) y usarlo en la instancia "PROD ECS BACKEND"
    * Dentro de la instancia "PROD EC2 BACKEND" configurar awscli usando el usuario programático a través del comando "aws configure" 

<br>

---

### A - Análisis y configuración de Security Groups

<br>

1. La aplicación desplegada está conformada por los siguientes componentes:

    * Frontend, desplegado en un bucket S3. El frontend actualmente apunta al puerto 80 de la IP Pública de la instancia "PROD BACKEND"
    * Backend, desplegado en la instancia "PROD BACKEND", escucha en el puerto 80 las solicitudes del bucket S3. Asimismo, se conecta a la instancia "PROD DB" a través del puerto 3306 usando el usuario "admin"
    * Base de datos, desplegado en la instancia "PROD DB", escucha en el puerto 3306 (MySQL) las solicitudes de la instancia "PROD BACKEND".

```bash
Usuario --(80)--> Bucket S3 --(80)--> PROD BACKEND --(3306)--> PROD DB MySQL
```


2. Los recursos desplegados en AWS tienen asignados los siguientes security groups. Todos los security groups tienen asignados ALL TRAFFIC al 0.0.0.0/0 tanto en entrada (Inbound rules) como en salida (Outbound rules):

    * PROD BACKEND (sg_app)
    * PROD DB (sg_app)
    * NAT Instances (sg_nat)


3. Generaremos los siguientes security groups. Además, **crearemos la instancia "PROD BASTION"** en la "SUBNET PUBLICA B"

    * PROD BACKEND (sg_app, sg_ssh)
    * PROD DB (sg_db, sg_ssh)
    * PROD BASTION (sg_prodbastion)


4. Respecto al sg_app de PROD BACKEND configuraremos lo siguiente:

    * **Inbound rules**
        * Type: HTTP
        * Source: 0.0.0.0/0
    * **Outbound rules**
        * Type: MySQL/Aurora
        * Destination: sg_db (ID) 


5. Respecto al sg_db de PROD DB configuraremos lo siguiente:

    * **Inbound rules**
        * Type: MySQL/Aurora
        * Source: sg_app (ID) 
    * **Outbound rules**
        * Sin reglas


6. Respecto al sg_ssh de las instancias PROD DB y PROD BACKEND configuraremos lo siguiente:

    * **Inbound rules**
        * Type: SSH
        * Source: sg_prodbastion
    * **Outbound rules**
        * Sin reglas


7. Respecto al sg_prodbastion de la instancia PROD BASTION configuraremos lo siguiente:

    * **Inbound rules**
        * Type: SSH
        * Source: MY_IP
    * **Outbound rules**
        * Type: SSH
        * Source: 192.168.0.0/16


8. Después de realizar las configuraciones anteriormente mencionadas validaremos los siguientes casos:

    * Nuestra aplicación seguirá funcionando. Ingresar un nuevo registro
    * Validar que desde la intstancia PROD BACKEND no podemos ingresar vía SSH a PROD DB
    * Validar que desde la instancia PROD BASTION podemos ingresar por SHH hacia las instancias PROD BACKEND y PROD DB


<img src="images/Lab04_01.jpg">

<br>