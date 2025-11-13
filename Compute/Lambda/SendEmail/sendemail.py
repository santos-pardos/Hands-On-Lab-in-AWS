import boto3
import json

# Replace with your SNS topic ARN
TOPIC_ARN = "arn:aws:sns:us-east-1:883822223160:S3-CV-SNS"

def lambda_handler(event, context):
    sns_client = boto3.client("sns")
    subject = "Test Email from Lambda"
    message = "This is a test notification sent via AWS Lambda and SNS."
    try:
        response = sns_client.publish(
            TopicArn=TOPIC_ARN,
            Message=message,
            Subject=subject
        )
        print("Notification sent successfully:", response)
        return {
            'statusCode': 200,
            'body': json.dumps('Message sent')
        }
    except Exception as e:
        print("Error sending SNS notification:", e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error sending message')
        }

