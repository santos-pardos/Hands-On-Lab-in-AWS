# AWS Solutions Architect Associate

### **Autor:** Jorge Barreto | AWSx10 & AWS Community Builder | [LinkedIn](https://www.linkedin.com/in/jorgebarretoolivos/)
<br>

**Objetivo:**

Este repositorio tiene por objetivo:
 * Desarrollar laboratorios paso a paso para entender, desde la práctica, los diferentes servicios de AWS
 * Desde la comprensión practica de los servicios, buscar obtener la certificación de AWS Solutions Architect Associate.

---

#### **Laboratorio 01: VPC & NAT**  [README-Lab01.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-01/README-Lab01.md)
* Construcción de una VPC usando subnet públicas (ruteando a través de un Internet Gateway) y subnets privadas (ruteando a través de un NAT Instances)
* Configuración de un NAT Instances

#### **Laboratorio 02: EBS & KMS** [README-Lab02.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-02/README-Lab02.md)
* Asociar volumen EBS
* Aumentar tamaño del volumen EBS
* Reconocimiento del servicio KMS (Key Mananagement Service)

#### **Laboratorio 03: EC2, AWSCLI, metadata & S3** [README-Lab03.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-03/README-Lab03.md)
* Instalación y configuración del Backend en la instancia EC2. Uso de AWSCLI y la metadata en la instancia EC2
* Configuración de "Static website hosting" en S3 (Front)
* Instalación y configuración de la base de datos en la instancia EC2.

#### **Laboratorio 04: Security Groups** [README-Lab04.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-04/README-Lab04.md)
* Análisis y configuración de Security Groups

#### **Laboratorio 05: Elastic IP** [README-Lab05.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-05/README-Lab05.md)
* Análisis y configuración de una Elastic IP

#### **Laboratorio 06: System Manager - Session Manager** [README-Lab06.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-06/README-Lab06.md)
* Configuración de System Manager - Session Manager en instancias Linux/Ubuntu
* Eliminación del security group sg_ssh de las instancias EC2
* Eliminación de la instancia PROD BASTION

#### **Laboratorio 07: VPC Flow Logs & Athena** [README-Lab07.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-07/README-Lab07.md)
* Habilitación de VPC Flow Logs
* Uso de Amazon Athena para la lectura de VPC Flow Logs

#### **Laboratorio 08: Network ACL** [README-Lab08.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-08/README-Lab08.md)
* Configuración de NACL (Network Access Control List)

#### **Laboratorio 09: VPC Endpoint Gateway & Interface** [README-Lab09.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-09/README-Lab09.md)
* Configuración de VPC Endpoint Gateway
* Configuración de VPC Endpoint Interface

#### **Laboratorio 10: VPC Peering Connection** [README-Lab10.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-10/README-Lab10.md)
* Configuración de Peering Connection

#### **Laboratorio 11: ALB (Application Load Balancer)** [README-Lab11.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-11/README-Lab11.md)
* Despliegue de una balanceador de aplicaciones (Application Load Balancer)

#### **Laboratorio 12: ALB (Application Load Balancer) & Sticky Session** [README-Lab12.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-12/README-Lab12.md)
* Configuración de Sticky Session en el Application Load Balancer (ALB)

#### **Laboratorio 13: ALB (Application Load Balancer) & Listener Rules** [README-Lab13.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-13/README-Lab13.md)
* Configuración del Listener Rules en el Application Load Balancer (ALB)

#### **Laboratorio 14: ALB (Application Load Balancer), Certificate Manager & Route53** [README-Lab14.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-14/README-Lab14.md)
* Creación de un certificado SSL/TLS y su asociación al Application Load Balancer

#### **Laboratorio 15: EC2 AutoScaling Group, Launch Configuration, SNS & CloudWatch Alarm** [README-Lab15.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-15/README-Lab15.md)
* Configuración de "EC2 AutoScaling Group" usando "Launch Configuration", "SNS" y "CloudWatch Alarm"

#### **Laboratorio 16: CloudFront & S3** [README-Lab16.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-16/README-Lab16.md)
* Despliegue de contenido estático en CloudFront
* Configuración de Cache con TTL 0 en CloudFront
* Identificar la configuración OAI (Origin Access Identities) en la distribución CloudFront y el bucket S3

#### **Laboratorio 17: CloudFront, S3 & OAI** [README-Lab17.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-17/README-Lab17.md)
* Despliegue de una distribución CloudFront usando como origen un bucket de S3
* Configurar OAC (Origin Access Control) en la distribución CloudFront y el bucket S3 

#### **Laboratorio 18: CloudFront, Certificate Manager & Route53** [README-Lab18.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-18/README-Lab18.md)
* Despliegue de una distribución CloudFront con dominio personalizado usando Route53 y certificado SSL/TLS con Certificate Manager

#### **Laboratorio 19: Route53 & Routing Policies** [README-Lab19.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-19/README-Lab19.md)
* Configuración del "Routing Policies Latency" en Route 53
* Configuración del "Routing Policies Weighted" en Route 53

#### **Laboratorio 20: IAM User Programmatic, SDK & IAM Roles** [README-Lab20.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-20/README-Lab20.md)
* Creación de un IAM User Programmatic
* Uso del SDK de Python (boto3)
* Uso de IAM roles

#### **Laboratorio 21: IAM & Evaluating permission levels** [README-Lab21.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-21/README-Lab21.md)
* Evaluando jerarquía de evaluación de permisos en IAM

#### **Laboratorio 22: AWS Organizations & Switch Role Account** [README-Lab22.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-22/README-Lab22.md)
* Crear una cuenta AWS a través del servicio AWS Organizations
* Hacer "Switch Role" entre cuentas de AWS desde la consola

#### **Laboratorio 23: IAM Roles & STS** [README-Lab23.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-23/README-Lab23.md)
* Entendimiento de STS (Secure Token Service)

#### **Laboratorio 24: AWS Organizations, OU & SCPs** [README-Lab24.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-24/README-Lab24.md)
* Entendimiento de OU (Organizational Unit) en AWS Organizations
* Entendimiento de SCPs (Service Control Policies) en AWS Organizations

#### **Laboratorio 25: EBS Performance** [README-Lab25.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-25/README-Lab25.md)
* Analizar métricas de performance en volúmenes EBS

#### **Laboratorio 26: EC2 Instances Store** [README-Lab26.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-26/README-Lab26.md)
* Configuración de volúmenes EC2 Instances Store (Volúmenes Efímeros)

#### **Laboratorio 27: CloudFormation - Mappings, Conditions & Parameters** [README-Lab27.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-27/README-Lab27.md)
* Desplegar un stack de CloudFormation multi-región usando "Mappings", "Conditions" y "Parameters"

#### **Laboratorio 28: S3 Presign - GetObject** [README-Lab28.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-28/README-Lab28.md)
* Entendimiento de AWS S3 Presign (Método GET)
* Entendimiento de AWS S3 Presign (Método POST y SDK Boto3 Python)

#### **Laboratorio 29: S3 CORS** [README-Lab29.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-29/README-Lab29.md)
* Configuración de Cross-origin resource sharing (CORS) en S3 (Permissions)

#### **Laboratorio 30: S3 Glacier & AWSCLI** [README-Lab30.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-30/README-Lab30.md)
* Subir archivos directamente a S3 Glacier usando AWSCLI

#### **Laboratorio 31: S3, Glue, Crawler & Athena** [README-Lab31.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-31/README-Lab31.md)
* Integración de S3, Glue, Crawler y Athena

#### **Laboratorio 32: EFS** [README-Lab32.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-32/README-Lab32.md)
* Configuración de un File System usando EFS en instancias Linux aprovisionadas en distintas VPCs

#### **Laboratorio 33: RDS & Secrets Manager** [README-Lab33.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-33/README-Lab33.md)
* Aprovisionamiento de una instancia RDS desde CloudFormation usando Secrets Manager como generador de credenciales

#### **Laboratorio 34: RDS Read Replica** [README-Lab34.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-34/README-Lab34.md)
* Configuración y análisis de la propiedad "Read Replica" en la instancia de RDS

#### **Laboratorio 35: RDS Multi-AZ** [README-Lab35.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-35/README-Lab35.md)
* Configuración y análisis de la propiedad "Multi-AZ" en la instancia de RDS

#### **Laboratorio 36: RDS Performance Insights** [README-Lab36.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-36/README-Lab36.md)
* Configuración de "Performance Insights" en la instancia de RDS.

#### **Laboratorio 37: Agente Unificado CloudWatch & System Manager (Parameter Store & Run Command)** [README-Lab37.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-37/README-Lab37.md)
* Instalación del "Agente Unificado CloudWatch" (Memoria, Espacio en disco y Logs) a través de "System Manager - Parameter Store" y "Run Command".

#### **Laboratorio 38: CloudWatch Event Rules, EC2, Tags & Lambda** [README-Lab38.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-38/README-Lab38.md)
* Configuración de "CloudWatch Event Rules (Schedule)" y el apagado/encendido automático de instancias EC2 con Tags usando Lambdas.

#### **Laboratorio 39: Event Bridge, EC2 (cripto-mining), GuardDuty y SNS** [README-Lab39.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-39/README-Lab39.md)
* Configuración de "Event Bridge (Rule with an event pattern)", "GuardDuty" y notificaciones "SNS" para identificación de amenazas en nuestra cuenta de AWS.

#### **Laboratorio 40: SQS (create,list,send,receive y delete)** [README-Lab40.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-40/README-Lab40.md)
* Configuración y gestión a través de los métodos create, list, send, receive, y delete de una cola SQS usando el SDK de Python (boto3) 

#### **Laboratorio 41: SQS (Visibility Timeout, Short Polling & Long Polling)** [README-Lab41.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-41/README-Lab41.md)
* Configuración de las propiedades "Visibility Timeout", "Long-polling" y "Short-polling" en una cola SQS 

#### **Laboratorio 42: SQS (Dead Letter Queue)** [README-Lab42.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-42/README-Lab42.md)
* Configuración de la propiedad "Dead Letter Queue" en una cola SQS 

#### **Laboratorio 43: SQS (Standard vs FIFO)** [README-Lab43.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-43/README-Lab43.md)
*  Configuración de un cola SQS FIFO y visualización del orden de envío de los mensajes
*  Configuración de una cola SQS Standard y visualización del orden de envío de los mensajes

#### **Laboratorio 44: SNS (Subscripción SQS y Lambda)** [README-Lab44.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-44/README-Lab44.md)
*  Creación de un tópico SNS y suscripción de una cola SQS y una función Lambda

#### **Laboratorio 45: Step Function (Integrando Lambda, DynamoDB y Amazon Rekognition)** [README-Lab45.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-45/README-Lab45.md)
*  Creación de una máquina de estado orquestando funciones Lambdas, tablas en DynamoDB e invocaciones con Amazon Rekognition

#### **Laboratorio 46: Cognito User Pool (Integración con CloudFront)** [README-Lab46.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-46/README-Lab46.md)
*  Implementación de Cognito User Pool & Grant Types

#### **Laboratorio 47: Cognito Identity Pool y STS** [README-Lab47.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-47/README-Lab47.md)
*  Obtención de credenciales temporales STS consumiendo el servicio de Cognito Identity Pool usando AWSCLIv2

#### **Laboratorio 48: Cognito User Pool (Integración con ALB)** [README-Lab48.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-48/README-Lab48.md)
*  Integración de Cognito User Pool y ALB (Application Load Balancer) a través de ALB Tokens

#### **Laboratorio 49: WAF (Integración con CloudFront, ApiGateway, Lambda y DynamoDB)** [README-Lab49.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-49/README-Lab49.md)
* Integración entre WAF y CloudFront usando API Gateway, Lambda y DynamoDB
* Configuración de AWS WAF web ACL Rules: “manual ip block rule” y “sqli rule”

#### **Laboratorio 50: CloudTrail (Integración con EventBridge, Lambda, IAM y SNS)** [README-Lab50.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-50/README-Lab50.md)
* Integrar los eventos de CloudTrail y Event Bridge 
* Automatizar la respuesta ante incidentes en usuarios IAM usando Lambda y SNS

#### **Laboratorio 51: AWS IAM Identity Center (AWS Single Sign-On)** [README-Lab51.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-51/README-Lab51.md)
* Habilitación del servicio "AWS IAM Identity Center (AWS Single Sign-On)" en AWS Organizations
* Configuración de IAM Identity Center (successor to AWS Single Sign-On)

#### **Laboratorio 52: KMS with plain text** [README-Lab52.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-52/README-Lab52.md)
* Cifrado y descifrado de un archivo de texto plano usando KMS "Customer managed keys"
* Cifrado y descifrado de un archivo de texto plano usando KMS "Customer managed keys" - Data Key

#### **Laboratorio 53: Amazon Polly** [README-Lab53.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-53/README-Lab53.md)
* Interactuar con la API de Amazon Polly

#### **Laboratorio 54: Amazon ECS, ECR, Secrets Manager y EFS (Elastic File System)** [README-Lab54.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-54/README-Lab54.md)
* Uso del servicio ECR (Elastic Container Registry), EFS y Secrets Manager y upload de una imagen Docker
* Creación de un cluster ECS-EC2 (Elastic Container Services) y uso de un task definition y services

#### **Laboratorio 55: Custom IAM Policies** [README-Lab55.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-55/README-Lab55.md)
* Accesos de usuarios IAM a determinados buckets S3 usando Custom IAM Policies

#### **Laboratorio 56: RDS Aurora** [README-Lab56.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-56/README-Lab56.md)
* Aprovisionamiento de una instancia RDS Aurora usando Secrets Manager como generador de credenciales











