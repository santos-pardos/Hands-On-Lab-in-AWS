import boto3

# Creating IAM connection
iam = boto3.client('iam')

# Fetch the list of existing user
for user in iam.list_users()['Users']:
 print("User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n".format(
 user['UserName'],
 user['UserId'],
 user['Arn'],
 user['CreateDate']
 )
 )
