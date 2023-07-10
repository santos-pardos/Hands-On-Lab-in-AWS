# AWS Solutions Architect Associate - Laboratorio 49

<br>

### Objetivo: 
* Integración entre WAF y CloudFront usando API Gateway, Lambda y DynamoDB
* Configuración de AWS WAF web ACL Rules: “manual ip block rule” y “sqli rule”

### Tópico:
* Compute
* Security, Identity & Compliance
* Database
* Application Integration

### Dependencias:
* Ninguna

<br>

---

### A - Integración entre WAF y API Gateway y configuración de ACLs “manual ip block rule” y “sqli rule”


<br>

1. Acceder al servicio AWS Cloud9 y generar un nuevo ambiente de trabajo (Ubuntu 18.04 LTS)

<br>

2. Ejecutar los siguientes comandos en nuestro Cloud9

```bash
#Ubuntu 18.04
sudo apt-get update
git clone https://github.com/jbarreto7991/aws-solutionsarchitectassociate.git
sam --version
```

<br>

3. Acceder al laboratorio 49 (Lab-49), carpeta "code". Validar que se cuenta con el archivo "1_lab49-waf.json" y la carpeta "SAM". Analizar el contenido de estos archivos.

<br>

4. Desplegar la plantilla CloudFormation **1_lab49-waf.json** ejecutando AWSCLI 

```bash
aws cloudformation create-stack --stack-name lab49-waf --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-49/code/1_lab49-waf.json
```

<br>

5. Desplegar la plantilla "SAM/template.yaml" usando "sam init" de SAM (Serverless Application Model) desde Cloud9. Seleccionar opción 2.

```bash
#Comando
cd /home/ubuntu/environment/aws-solutionsarchitectassociate/Lab-49/code/SAM/
sam init

#Mensaje SAM
Which template source would you like to use?
        1 - AWS Quick Start Templates
        2 - Custom Template Location

#Responder
Choice:2

#Mensaje SAM
Template location (git, mercurial, http(s), zip, path):

#Responder
/home/ubuntu/environment/aws-solutionsarchitectassociate/Lab-49/code/SAM/sam-app.zip

#Mensaje SAM
-----------------------
Generating application:
-----------------------
Location: /home/ubuntu/environment/aws-solutionsarchitectassociate/Lab-49/code/SAM/sam-app.zip
Output Directory: .
    
SAM CLI update available (1.61.0); (1.33.0 installed)
To download: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html
```

<br>

6. Desplegar la plantilla "SAM/template.yaml" usando "sam build" de SAM (Serverless Application Model)

```bash
#Comando
sam build

#Mensaje SAM
Building codeuri: /home/ubuntu/environment/aws-solutionsarchitectassociate/Lab-49/code/SAM/dynamo-handler runtime: nodejs12.x metadata: {} architecture: x86_64 functions: ['DDBHandlerFunction']
package.json file not found. Continuing the build without dependencies.
Running NodejsNpmBuilder:CopySource

Build Succeeded

Built Artifacts  : .aws-sam/build
Built Template   : .aws-sam/build/template.yaml

Commands you can use next
=========================
[*] Invoke Function: sam local invoke
[*] Deploy: sam deploy --guided
```

<br>

7. Desplegar la plantilla "SAM/template.yaml" usando "sam deploy --guided" de SAM (Serverless Application Model). Ingresar los siguientes valores:

    * Stack Name [sam-app]: Enter
    * AWS Region [us-east-1]: Enter
    * Confirm changes before deploy [Y/n]: Y
    * Allow SAM CLI IAM role creation [Y/n]: Y
    * DDBHandlerFunction may not have authorization defined, Is this okay? [y/N]: y
    * DDBHandlerFunction may not have authorization defined, Is this okay? [y/N]: y
    * DDBHandlerFunction may not have authorization defined, Is this okay? [y/N]: y
    * DDBHandlerFunction may not have authorization defined, Is this okay? [y/N]: y
    * Save arguments to configuration file [Y/n]: Y
    * SAM configuration file [samconfig.toml]: Enter
    * SAM configuration environment [default]: Enter
    
    * Deploy this changeset? [y/N]: y

<br>

```bash
#Comando
sam deploy --guided

#Comando y Mensaje SAM. Respuesta al final de cada mensaje

Configuring SAM deploy
======================

        Looking for config file [samconfig.toml] :  Found
        Reading default arguments  :  Success

        Setting default arguments for 'sam deploy'
        =========================================
        Stack Name [sam-app]: 
        AWS Region [us-east-1]: 
        #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
        Confirm changes before deploy [Y/n]: Y
        #SAM needs permission to be able to create roles to connect to the resources in your template
        Allow SAM CLI IAM role creation [Y/n]: Y
        DDBHandlerFunction may not have authorization defined, Is this okay? [y/N]: y
        DDBHandlerFunction may not have authorization defined, Is this okay? [y/N]: y
        DDBHandlerFunction may not have authorization defined, Is this okay? [y/N]: y
        DDBHandlerFunction may not have authorization defined, Is this okay? [y/N]: y
        Save arguments to configuration file [Y/n]: Y
        SAM configuration file [samconfig.toml]: 
        SAM configuration environment [default]: 

        Looking for resources needed for deployment:
        Creating the required resources...
        Successfully created!
         Managed S3 bucket: aws-sam-cli-managed-default-samclisourcebucket-1gdcb56rx7r6e
         A different default S3 bucket can be set in samconfig.toml

        Saved arguments to config file
        Running 'sam deploy' for future deployments will use the parameters saved above.
        The above parameters can be changed by modifying samconfig.toml
        Learn more about samconfig.toml syntax at 
        https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-config.html

Uploading to sam-app/e972c01900de2ca33a1df902d6a5f057  675 / 675  (100.00%)

        Deploying with following values
        ===============================
        Stack name                   : sam-app
        Region                       : us-east-1
        Confirm changeset            : True
        Deployment s3 bucket         : aws-sam-cli-managed-default-samclisourcebucket-1gdcb56rx7r6e
        Capabilities                 : ["CAPABILITY_IAM"]
        Parameter overrides          : {}
        Signing Profiles             : {}

Initiating deployment
=====================
Uploading to sam-app/5c9bb5e9a117b950770c09456205f0f8.template  1524 / 1524  (100.00%)

Waiting for changeset to be created..

CloudFormation stack changeset
-----------------------------------------------------------------------------------------------------------------------------------------------------
Operation                             LogicalResourceId                     ResourceType                          Replacement                         
-----------------------------------------------------------------------------------------------------------------------------------------------------
+ Add                                 DDBHandlerFunctionCreateOrUpdateIte   AWS::Lambda::Permission               N/A                                 
                                      mPermissionProd                                                                                                 
+ Add                                 DDBHandlerFunctionDeleteAnItemPermi   AWS::Lambda::Permission               N/A                                 
                                      ssionProd                                                                                                       
+ Add                                 DDBHandlerFunctionGetAllItemsPermis   AWS::Lambda::Permission               N/A                                 
                                      sionProd                                                                                                        
+ Add                                 DDBHandlerFunctionGetAnItemPermissi   AWS::Lambda::Permission               N/A                                 
                                      onProd                                                                                                          
+ Add                                 DDBHandlerFunctionRole                AWS::IAM::Role                        N/A                                 
+ Add                                 DDBHandlerFunction                    AWS::Lambda::Function                 N/A                                 
+ Add                                 ItemsTable                            AWS::DynamoDB::Table                  N/A                                 
+ Add                                 ServerlessRestApiDeployment5df6f31e   AWS::ApiGateway::Deployment           N/A                                 
                                      3b                                                                                                              
+ Add                                 ServerlessRestApiProdStage            AWS::ApiGateway::Stage                N/A                                 
+ Add                                 ServerlessRestApi                     AWS::ApiGateway::RestApi              N/A                                 
-----------------------------------------------------------------------------------------------------------------------------------------------------

Changeset created successfully. arn:aws:cloudformation:us-east-1:XXXXXXXXXXXX:changeSet/samcli-deploy1667351522/90ccdc22-c839-455b-89cb-3883b3a7567e


Previewing CloudFormation changeset before deployment
======================================================
Deploy this changeset? [y/N]: y

XXXX-XX-XX XX:XX:XX - Waiting for stack create/update to complete

CloudFormation events from changeset
-----------------------------------------------------------------------------------------------------------------------------------------------------
ResourceStatus                        ResourceType                          LogicalResourceId                     ResourceStatusReason                
-----------------------------------------------------------------------------------------------------------------------------------------------------
CREATE_IN_PROGRESS                    AWS::DynamoDB::Table                  ItemsTable                            -                                   
CREATE_IN_PROGRESS                    AWS::DynamoDB::Table                  ItemsTable                            Resource creation Initiated         
CREATE_COMPLETE                       AWS::DynamoDB::Table                  ItemsTable                            -                                   
CREATE_IN_PROGRESS                    AWS::IAM::Role                        DDBHandlerFunctionRole                Resource creation Initiated         
CREATE_IN_PROGRESS                    AWS::IAM::Role                        DDBHandlerFunctionRole                -                                   
CREATE_COMPLETE                       AWS::IAM::Role                        DDBHandlerFunctionRole                -                                   
CREATE_IN_PROGRESS                    AWS::Lambda::Function                 DDBHandlerFunction                    -                                   
CREATE_IN_PROGRESS                    AWS::Lambda::Function                 DDBHandlerFunction                    Resource creation Initiated         
CREATE_COMPLETE                       AWS::Lambda::Function                 DDBHandlerFunction                    -                                   
CREATE_IN_PROGRESS                    AWS::ApiGateway::RestApi              ServerlessRestApi                     -                                   
CREATE_IN_PROGRESS                    AWS::ApiGateway::RestApi              ServerlessRestApi                     Resource creation Initiated         
CREATE_COMPLETE                       AWS::ApiGateway::RestApi              ServerlessRestApi                     -                                   
CREATE_IN_PROGRESS                    AWS::Lambda::Permission               DDBHandlerFunctionGetAnItemPermissi   -                                   
                                                                            onProd                                                                    
CREATE_IN_PROGRESS                    AWS::Lambda::Permission               DDBHandlerFunctionCreateOrUpdateIte   -                                   
                                                                            mPermissionProd                                                           
CREATE_IN_PROGRESS                    AWS::Lambda::Permission               DDBHandlerFunctionGetAnItemPermissi   Resource creation Initiated         
                                                                            onProd                                                                    
CREATE_IN_PROGRESS                    AWS::Lambda::Permission               DDBHandlerFunctionCreateOrUpdateIte   Resource creation Initiated         
                                                                            mPermissionProd                                                           
CREATE_IN_PROGRESS                    AWS::Lambda::Permission               DDBHandlerFunctionGetAllItemsPermis   -                                   
                                                                            sionProd                                                                  
CREATE_IN_PROGRESS                    AWS::ApiGateway::Deployment           ServerlessRestApiDeployment5df6f31e   -                                   
                                                                            3b                                                                        
CREATE_IN_PROGRESS                    AWS::Lambda::Permission               DDBHandlerFunctionDeleteAnItemPermi   -                                   
                                                                            ssionProd                                                                 
CREATE_IN_PROGRESS                    AWS::Lambda::Permission               DDBHandlerFunctionDeleteAnItemPermi   Resource creation Initiated         
                                                                            ssionProd                                                                 
CREATE_IN_PROGRESS                    AWS::Lambda::Permission               DDBHandlerFunctionGetAllItemsPermis   Resource creation Initiated         
                                                                            sionProd                                                                  
CREATE_IN_PROGRESS                    AWS::ApiGateway::Deployment           ServerlessRestApiDeployment5df6f31e   Resource creation Initiated         
                                                                            3b                                                                        
CREATE_COMPLETE                       AWS::ApiGateway::Deployment           ServerlessRestApiDeployment5df6f31e   -                                   
                                                                            3b                                                                        
CREATE_IN_PROGRESS                    AWS::ApiGateway::Stage                ServerlessRestApiProdStage            -                                   
CREATE_IN_PROGRESS                    AWS::ApiGateway::Stage                ServerlessRestApiProdStage            Resource creation Initiated         
CREATE_COMPLETE                       AWS::ApiGateway::Stage                ServerlessRestApiProdStage            -                                   
CREATE_COMPLETE                       AWS::Lambda::Permission               DDBHandlerFunctionCreateOrUpdateIte   -                                   
                                                                            mPermissionProd                                                           
CREATE_COMPLETE                       AWS::Lambda::Permission               DDBHandlerFunctionDeleteAnItemPermi   -                                   
                                                                            ssionProd                                                                 
CREATE_COMPLETE                       AWS::Lambda::Permission               DDBHandlerFunctionGetAnItemPermissi   -                                   
                                                                            onProd                                                                    
CREATE_COMPLETE                       AWS::Lambda::Permission               DDBHandlerFunctionGetAllItemsPermis   -                                   
                                                                            sionProd                                                                  
CREATE_COMPLETE                       AWS::CloudFormation::Stack            sam-app                               -                                   
-----------------------------------------------------------------------------------------------------------------------------------------------------

CloudFormation outputs from deployed stack
------------------------------------------------------------------------------------------------------------------------------------------------------
Outputs                                                                                                                                              
------------------------------------------------------------------------------------------------------------------------------------------------------
Key                 Function                                                                                                                         
Description         DynamoDB handler function ARN                                                                                                    
Value               arn:aws:lambda:us-east-1:XXXXXXXXXXXX:function:sam-app-DDBHandlerFunction-ZBxrnpfeDXfP                                           

Key                 ApiEndpoint                                                                                                                      
Description         The invoke URL for our HTTP API                                                                                                  
Value               https://psb5d4fxu6.execute-api.us-east-1.amazonaws.com/items                                                                     
------------------------------------------------------------------------------------------------------------------------------------------------------

Successfully created/updated stack - sam-app in us-east-1

```

<br>

8. Guardar en variable de entorno el endpoint del API Gateway desplegado. Este valor se encuentra en la sección "Outputs" del paso anterior para "Key:ApiEndpoint"

```bash
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Outputs                                                                                                                                                                               
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Key                 Function                                                                                                                                                          
Description         DynamoDB handler function ARN                                                                                                                                     
Value               arn:aws:lambda:us-east-1:068242378542:function:sam-app-DDBHandlerFunction-voEHcJzRYOO8                                                                            

Key                 ApiEndpoint                                                                                                                                                       
Description         The invoke URL for our HTTP API                                                                                                                                   
Value               https://7wqpx1agna.execute-api.us-east-1.amazonaws.com/items                                                                                                      
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

<br>

```bash
API_GATEWAY=https://psb5d4fxu6.execute-api.us-east-1.amazonaws.com
echo $API_GATEWAY
```

<br>

9. Testear nuestro API Gateway a través de los siguientes comandos en Cloud9

```bash
#To create or update an item
curl -v -X "PUT" -H "Content-Type: application/json" -d "{\"id\": \"1\", \"price\": 1, \"name\": \"myitem1\"}" $API_GATEWAY/items
curl -v -X "PUT" -H "Content-Type: application/json" -d "{\"id\": \"2\", \"price\": 2, \"name\": \"myitem2\"}" $API_GATEWAY/items
curl -v -X "PUT" -H "Content-Type: application/json" -d "{\"id\": \"3\", \"price\": 3, \"name\": \"myitem3\"}" $API_GATEWAY/items
curl -v -X "PUT" -H "Content-Type: application/json" -d "{\"id\": \"4\", \"price\": 4, \"name\": \"myitem4\"}" $API_GATEWAY/items
curl -v -X "PUT" -H "Content-Type: application/json" -d "{\"id\": \"5\", \"price\": 5, \"name\": \"myitem5\"}" $API_GATEWAY/items

#To get all items
curl -v $API_GATEWAY/items

#To get an item
curl -v $API_GATEWAY/items/4
curl -v $API_GATEWAY/items/5

#To delete an item and validation
curl -v -X "DELETE" $API_GATEWAY/items/1
curl -v $API_GATEWAY/items
```

<br>

10. A través de la consola de AWS analizar los recursos aprovisionados en los servicios de:
    - API Gateway
    - DynamoDB
    - Lambda

<br>

11. Accedemos al servicio CloudFront creando una distribución con las siguientes configuraciones. Considerar los valores no mencionados a continuación en default. Al finalizar la configuración dar clic en el botón "Create distribution"

    - Origin
        - Origin domain: psb5d4fxu6.execute-api.us-east-1.amazonaws.com ($API_GATEWAY)
        - Protocol: HTTPS Only
            - Minimum origin SSL protocol: TLSv1.2
        - Origin path - optional: "No colocar ningún path"
        - Name: apigateway-httpapi
    - Default cache behavior
        - Viewer
            - Viewer protocol policy: Redirect HTTP to HTTPS
            - Allowed HTTP methods: GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE
    - Cache key and origin requests
        - Cache policy and origin request policy (recommended)
            - Cache policy: CachingDisabled

 
<br>

<img src="images/Lab49_01.jpg">

<br>

<img src="images/Lab49_02.jpg">

<br>

<img src="images/Lab49_03.jpg">

<br>

<img src="images/Lab49_04.jpg">

<br>


12. Testear nuestro API Gateway desde CloudFront a través de los siguientes comandos en Cloud9

```bash
#Variable DIST_CLOUDFRONT
DIST_CLOUDFRONT=https://d25wfgg7bxkfk5.cloudfront.net
echo $DIST_CLOUDFRONT

#To create or update an item
curl -v -X "PUT" -H "Content-Type: application/json" -d "{\"id\": \"6\", \"price\": 6, \"name\": \"myitem6\"}" $DIST_CLOUDFRONT/items
curl -v -X "PUT" -H "Content-Type: application/json" -d "{\"id\": \"7\", \"price\": 7, \"name\": \"myitem7\"}" $DIST_CLOUDFRONT/items
curl -v -X "PUT" -H "Content-Type: application/json" -d "{\"id\": \"8\", \"price\": 8, \"name\": \"myitem8\"}" $DIST_CLOUDFRONT/items
curl -v -X "PUT" -H "Content-Type: application/json" -d "{\"id\": \"9\", \"price\": 9, \"name\": \"myitem9\"}" $DIST_CLOUDFRONT/items
curl -v -X "PUT" -H "Content-Type: application/json" -d "{\"id\": \"10\", \"price\": 10, \"name\": \"myitem10\"}" $DIST_CLOUDFRONT/items

#To get all items
curl -v $DIST_CLOUDFRONT/items

#To get an item
curl -v $DIST_CLOUDFRONT/items/9
curl -v $DIST_CLOUDFRONT/items/10

#To delete an item and validation
curl -v -X "DELETE" $DIST_CLOUDFRONT/items/5
curl -v $DIST_CLOUDFRONT/items
```

<br>

13. Validamos que nuestra plantilla de CloudFormation sobre WAF esté desplegada. Accedemos a nuestra distribución CloudFront, desde la pestaña "General" damos clic en el botón "Edit". Luego, seleccionamos nuestro "AWS WAF web ACL" en la opción del mismo nombre. Guardamos la nueva configuración y esperamos el despliegue de nuestra distribución CloudFront.

<br>

<img src="images/Lab49_05.jpg">

<br>

<img src="images/Lab49_06.jpg">

<br>

14. Finalizado el despliegue de nuestra distribución CloudFront, accedemos a Cloud9 y ejecutamos los siguientes comandos. Analizar los resultados. Validar las mismas acciones desde el navegador.

```bash

#To get all items
curl -v $DIST_CLOUDFRONT/items

#To get an item
curl -v $DIST_CLOUDFRONT/items/9
curl -v $DIST_CLOUDFRONT/items/9%or%1'='1
```

<br>

<img src="images/Lab49_07.jpg">

<br>

<img src="images/Lab49_09.jpg">

<br>

15. Accedemos al servicio WAF y ejecutamos las siguientes acciones:

    - Clic en "Switch to AWS WAF Classic"
    - Ir a la opción "IP addresses"
    - En el campo "Filter" seleccionar "Global (CloudFront)"
    - Dar clic en la opción "Manual IP Block Set"
    - Dar clic en la opción "Add IP addresses or ranges"
    - Agregar nuestra IP Pública en el campo "Address". Agregar "/32" al final de nuestra IP
    - Dar clic en "Add IP address or range"
    - Dar clic en el botón "Add"

<br>

<img src="images/Lab49_10.jpg">

<br>

<img src="images/Lab49_11.jpg">

<br>

<img src="images/Lab49_12.jpg">

<br>

16. Ejecutamos los siguientes comandos. Analizar los resultados. Validar las mismas acciones desde el navegador.

```bash

#To get all items
curl -v $DIST_CLOUDFRONT/items

#To get an item
curl -v $DIST_CLOUDFRONT/items/9
```

<br>

<img src="images/Lab49_08.jpg">

<br>


---

### Eliminación de recursos

```bash
Deshabilitar Distribución CloudFront (Disable)
Eliminar Distribución CloudFront (Delete)
aws cloudformation delete-stack --stack-name lab49-waf
Desde Cloud9 ejecutar: "sam delete". Confirmar con "Y" en preguntas 
```