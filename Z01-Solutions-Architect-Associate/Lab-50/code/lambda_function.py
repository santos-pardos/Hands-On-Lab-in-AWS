import json
import boto3

#Conexión a AWS Services
iam = boto3.client('iam')
sns = boto3.client('sns')

def lambda_handler(event, context):
    # TODO implement
    print(event)
    print(context)

    """Obtener el nombre del usuario IAM y la politica asociada"""
    userName = event['detail']['requestParameters']['userName']
    policyArn = event['detail']['requestParameters']['policyArn']
    print(userName)
    print(policyArn)
    
    if policyArn=="arn:aws:iam::aws:policy/AdministratorAccess":
        detach_user_policy(userName,policyArn)
        message = {
            'userName': userName,
            'policyArn': policyArn,
            'message': 'Usuario con permisos de AdministratorAccess identificado',
            'action': 'Eliminar permiso AdministratorAccess del usuario'
        }
        publish_message(message)
        print("OK")
    else:
        pass
        

def detach_user_policy(username, policy_arn):
    response_iam=iam.detach_user_policy(
        UserName=str(username),
        PolicyArn=str(policy_arn)    
    )
    print(response_iam)
    print(f"Politica {policy_arn} desasociada del usuario {username}")

def publish_message(message): 
    response_sns = sns.publish(
        TargetArn="<ARN_SNS_TOPIC>",
        Message=json.dumps({'default': json.dumps(message)}),
        MessageStructure='json'
    )
    print(response_sns)
