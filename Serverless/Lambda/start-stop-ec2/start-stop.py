import boto3
region = 'eu-west-1'
  instances = ['i-0d6a9b386e8e2553a']
# instances = ['i-049eb3775de4a3d2d']
ec2 = boto3.client('ec2', region_name=region)
def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
#    ec2.start_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))