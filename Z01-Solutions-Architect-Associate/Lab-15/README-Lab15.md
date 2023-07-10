# AWS Solutions Architect Associate - Laboratorio 15

<br>

### Objetivo: 
* Configuración de "EC2 AutoScaling Group" usando "Launch Configuration", "SNS" y "CloudWatch Alarm"

### Tópico:
* Compute
* Management & Governance

### Dependencias:
* Ninguna

<br>

---

### A - Configuración de "EC2 AutoScaling Group" usando "Launch Configuration", "SNS" y "CloudWatch Alarm"


<br>

1. Debemos tener una llave Key Pair disponible. De no ser así, acceder al servicio EC2 y luego a la opción "Key Pair". Generar llave RSA y .pem 

<br>

2. Acceder al servicio AWS Cloud9 y generar un nuevo ambiente de trabajo (Ubuntu 18.04 LTS)

<br>

3. Ejecutar los siguinentes comandos en nuestro Cloud9

```bash
#Ubuntu 18.04
sudo apt-get update
git clone https://github.com/jbarreto7991/aws-solutionsarchitectassociate.git
```

<br>

4. Acceder al laboratorio 15 (Lab-15), carpeta "code". Validar que se cuenta con tres archivos CloudFormation: "1_lab15-vpc.yaml", "2_lab15-ec2.yaml" y "3_lab15_alb_targetgroup". Analizar el contenido de estos archivos.

<br>

5. Desplegar cada plantilla CloudFormation ejecutando AWSCLI. Considerar los parámetros a ser ingresados.

<br>

6. **1_lab15-vpc.yaml** (Esperar el despliegue total de esta plantilla cloudformation para continuar con las siguientes plantillas). En la sección "ParameterValue", ingresar el nombre del KeyPair creado en el paso 1. Esta plantilla creará la VPC "192.168.0.0/16", 06 Subnets dentro de este CIDR, un NAT Instances y demás componentes de red. No deberán existir redes existentes en este rango de IPs. Validar la creación del Stack desde la consola AWS a través del servicio AWS CloudFormation. El siguiente comando considera el valor "aws-solutionsarchitectassociate" para el KeyPair, reemplazar el nombre según la llave respectiva.

```bash
aws cloudformation create-stack --stack-name lab15-vpc --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-15/code/1_lab15-vpc.yaml --parameters ParameterKey=KeyPair,ParameterValue="aws-solutionsarchitectassociate" --capabilities CAPABILITY_IAM
```

<br>

7. **2_lab15-ec2.yaml** (Esperar el despliegue total de esta plantilla cloudformation para continuar con la siguiente plantilla). En la sección "Parameters", ingresar el nombre del KeyPair creado en el paso 1. Esta plantilla creará una instancia EC2. Se estará generando una AMI al final del proceso de creación de la instancia.

```bash
aws cloudformation create-stack --stack-name lab15-ec2 --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-15/code/2_lab15-ec2.yaml --parameters ParameterKey=KeyPair,ParameterValue="aws-solutionsarchitectassociate" --capabilities CAPABILITY_IAM
```

<br>

8. En el despliegue de recursos a través de CloudFormation se han generado 6 subnets: 2 subnets públicas (a ser usadas por el BALANCEADOR), 2 subnets privadas (donde han sido desplegada un EC2 INSTANCE BACKEND) y otras 2 subnets privadas que actualmente no tiene uso, pero serán destinadas en los siguientes laboratorios para la base de datos.

<br>

9. **3_lab15-alb-targetgroup.yaml**. Esta plantilla no tiene parámetros por ingresar. Generará un target group y un balanceador de aplicaciones. Además, la instancia EC2 se asociará al target group en el puerto 80.

```bash
aws cloudformation create-stack --stack-name lab15-alb-targetgroup --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-15/code/3_lab15-alb-targetgroup.yaml
```

<br>

10. Con la ejecución de estas tres plantillas, tenemos nuestro laboratorio base construido.

<br>

11. Generar manualmente una AMI desde la instancia EC2. Esperar a que el status cambie de "Pending" a "Available". Esto es visualizable desde la opción Images/AMIs

<br>

12. Accedemos al DNS Name del balanceador de aplicaciones para visualizar nuestra aplicación

<br>

<img src="images/Lab15_03.jpg">

<br>

13. Accedemos al servicio EC2, luego a la opción "Launch Configurations (en la sección AutoScaling)". Seguidamente, dar clic en el botón "Create launch configuration". Ingresamos los siguientes valores, luego dar clic en el botón "Create launch configuration"

    * Launch configuration name: lc-app
    * AMI: AMI generada en el paso 11
    * Instances Type: t2.micro
    * IAM Instance Profile: lab15-ec2-BackendIAMServerProfile
    * Security Groups: Select an existing security group
        * lab15-ec2-EC2SecurityWeb
    * Key Pair options: Choose and existing key pair
        * Existing key pair: aws-solutionsarchitectassociate (Generado en el paso 1)
    * Enable check "I acknowledge that I have access to the selected private key file (aws-solutionsarchitectassociate.pem), and that without this file, I won't be able to log into my instance."

<br>

<img src="images/Lab15_04.jpg">

<br>

<img src="images/Lab15_05.jpg">

<br>

<img src="images/Lab15_06.jpg">

<br>

<img src="images/Lab15_07.jpg">

<br>

<img src="images/Lab15_08.jpg">

<br>

<img src="images/Lab15_09.jpg">

<br>


14. Ingresamos al servicio SNS y damos clic en el botón "Create topic". Seleccionamos/ingresamos la siguiente información y damos clic en el botón "Create topic"

    * Type: Standard
    * Name: prod

<br>

<img src="images/Lab15_18.jpg">

<br>

<img src="images/Lab15_19.jpg">

<br>

15. Ingresamos a la opción "Subscriptions" y damos clic en el botón "Create subscription". Seleccionamos/ ingresamos la siguiente información y luego damos clic en el botón "Create Subscription". Llegará una notificación al correo electrónico ingresado, deberemos aceptar la subscripción. Cambiará el estado de nuestra subscripción SNS a " Confirmed" 

    * Protocol: Email
    * Endpoint: email@email.com

<br>

<img src="images/Lab15_21.jpg">

<br>

<img src="images/Lab15_22.jpg">

<br>

<img src="images/Lab15_23.jpg">

<br>


16. Accedemos al servicio EC2, luego a la opción "Auto Scaling Groups (en la sección AutoScaling)". Seguidamente, dar clic en el botón "Create Auto Scaling group". Ingresamos los siguientes valores, luego dar clic en el botón "Create Auto Scaling Groups"

    * Step 1 - Choose launch template or configuration
        * Auto Scaling group name: asg-app
        (Clic en Switch to launch configuration)
        * Launch configuration: lc-app
    * Step 2 - Choose instance launch options
        * VPC: PROD VPC
        * Availability Zones and subnets:
            * SUBNET PRIVATE BACKEND AZ A
            * SUBNET PRIVATE BACKEND AZ B
    * Step 3 - Configure advanced options
        * Load balancing: Attach to an existing load balancer
        * Attach to an existing load balancer: Choose from your load balancer target groups
        * Existing load balancer target groups: EC2LoadBalancerTargetGroupApp | HTTP
        * Health check grace period: 30
    * Step 4 - Configure group size and scaling policies
        * Group size:
            * Desired capacity: 2
            * Minimum capacity: 2
            * Maximum capacity: 5
        * Scaling policies: None
    * Step 5 - Add notifications
        * SNS Topic: prod
        * Event Types:
            * Launch
            * Terminate
            * Fail to launch
            * Fail to terminate
    * Step 6 - Add tags
            * Name: PROD ASG BACKEND

<br>

<img src="images/Lab15_10.jpg">

<br>

<img src="images/Lab15_11.jpg">

<br>

<img src="images/Lab15_12.jpg">

<br>

<img src="images/Lab15_13.jpg">

<br>

<img src="images/Lab15_14.jpg">

<br>

<img src="images/Lab15_15.jpg">

<br>

<img src="images/Lab15_16.jpg">

<br>

<img src="images/Lab15_17.jpg">

<br>

<img src="images/Lab15_24.jpg">

<br>

<img src="images/Lab15_25.jpg">

<br>

17. Accedemos al servicio EC2, luego a la opción "Instances" y validamos que se han generado dos instancias EC2 con el nombre "PROD ASG BACKEND". Asi mismo, estas dos instancias se han asociado al target group "EC2LoadBalancerTargetGroupApp". Al consultar el DNS Name de nuestro balanceador observaremos el contenido de 3 instancias (PROD ASG BACKEND 1, PROD ASG BAKEND 2 y PROD BACKEND AZ A)

<br>

<img src="images/Lab15_26.jpg">

<br>

<img src="images/Lab15_27.jpg">

<br>


18. Procedemos a eliminar la instancia "PROD BACKEND AZ A". Ejecutamos el siguiente comando en Cloud9

```bash
aws ec2 terminate-instances --instance-ids $(aws ec2 describe-instances --query 'Reservations[].Instances[].InstanceId' --filters "Name=tag:Name,Values=PROD BACKEND AZ A" --output text)
```

<br>

19. Ingresamos al servicio CloudWatch, seguido a la opción "CloudWatch Alarm" y luego damos clic en el botón "Create Alarm". Damos clic en "Select metric" e ingresamos a "EC2 > By AutoScaling Group". Filtramos por "asg-app" y seleccionamos la métrica "CPUUtilization". Dar clic en "Select metric". Ingresamos/seleccionamos los siguientes valores, al finalizar el proceso dar clic en "Create alarm". 

    * Metric
        * Metric name: CPUUtilization
        * AutoScalingGroupName: asg-app
        * Statistic: Average
        * Period: 1 minute
    * Conditions
        * Static
        * Whenever CPUUtilization is...: Greater/Equal
        * than…: 70
        * Datapoints to alarm: 3 out o 3
    * Notification
        * Alarm state trigger: In alarm
        * Send a notification to the following SNS topic: Select an existing SNS topic
        * Send a notification to…: prod
    * Name and description
        * Alarm name: app_cpu_up


<br>

<img src="images/Lab15_28.jpg">

<br>

<img src="images/Lab15_29.jpg">

<br>

<img src="images/Lab15_30.jpg">

<br>

<img src="images/Lab15_31.jpg">

<br>

<img src="images/Lab15_32.jpg">

<br>

<img src="images/Lab15_33.jpg">

<br>

<img src="images/Lab15_34.jpg">

<br>


20. Repetimos la mayoría de los pasos del numeral 19 con el objetivo de crear la alarma "app_cpu_down". Ingresamos/seleccionamos los siguientes valores, al finalizar el proceso dar clic en "Create alarm". Después de pocos minutos, el estado de la alarma cambiará de "Insufficient data" al estado respectivo. 

    * Metric
        * Metric name: CPUUtilization
        * AutoScalingGroupName: asg-app
        * Statistic: Average
        * Period: 1 minute
    * Conditions
        * Static
        * Whenever CPUUtilization is...: Lower/Equal
        * than…: 30
        * Datapoints to alarm: 3 out o 3
    * Notification
        * Alarm state trigger: In alarm
        * Send a notification to the following SNS topic: Select an existing SNS topic
        * Send a notification to…: prod
    * Name and description
        * Alarm name: app_cpu_down


<br>

<img src="images/Lab15_35.jpg">

<br>

<img src="images/Lab15_36.jpg">

<br>


21. Accedemos a la opción "Auto Scaling Groups" en la sección "Auto Scaling" en el servicio de EC2. Ingremos al autoscaling group previamente generado "asg-app". Nos dirigimos a la opción "Automatic Scaling" y damos clic en el botón "Create dynamic scaling policy". Ingresamos/seleccionamos los siguientes valores. Dar clic en el botón "Create"

    * Policy type: Step scaling
    * Scaling policy name: policy_up
    * CloudWatch alarm: app_cpu_up
    * Take the action: add
        * 1 capacity units when 70 <= CPUUtilization < 80
        * 1 capacity units when 80 <= CPUUtilization < 90
        * 1 capacity units when 70 <= CPUUtilization < +infinity
    * Instances need 10 seconds warm up before including in metric


<br>

<img src="images/Lab15_37.jpg">

<br>

<img src="images/Lab15_38.jpg">

<br>

<img src="images/Lab15_39.jpg">

<br>



22. Repetimos los pasos detallados anteriormente e ngresamos/seleccionamos los siguientes valores con el objetivo de crear la política de autoscaling "policy_down".

    * Policy type: Step scaling
    * Scaling policy name: policy_down
    * CloudWatch alarm: app_cpu_down
    * Take the action: Remove
        * 1 capacity units when 30 >= CPUUtilization > 20
        * 1 capacity units when 20 >= CPUUtilization > -infinity


<br>

<img src="images/Lab15_40.jpg">

<br>


23. Ingresamos a cada instancia "PROD ASG BACKEND" aprovisionada y ejecutamos los siguientes comandos con el objetivo de estresar la CPU.

```bash
sudo amazon-linux-extras install epel -y
sudo yum install stress -y
stress -c 4
```

<br>

<img src="images/Lab15_41.jpg">

<br>


24. Revisaremos el detalle de las métricas creadas anteriormente (app_cpu_up y app_cpu_down), el resumen de AutoScaling Group (asg_app), el target group (EC2LoadBalancerTargetGroupApp) y nuestra bandeja de correo electrónico.

<br>

<img src="images/Lab15_42.jpg">

<br>

<img src="images/Lab15_43.jpg">

<br>

<img src="images/Lab15_44.jpg">

<br>

<img src="images/Lab15_45.jpg">

<br>

<img src="images/Lab15_46.jpg">

<br>


### Eliminación de recursos

```bash
aws cloudformation delete-stack --stack-name lab15-alb-targetgroup
aws cloudformation delete-stack --stack-name lab15-ec2
aws cloudformation delete-stack --stack-name lab15-vpc
```