import json
import base64
import boto3
import email
def lambda_handler(event, context):
    s3 = boto3.client("s3")
    
    client = boto3.client('sns')
# decoding form-data into bytes
    post_data = base64.b64decode(event["body"])
    # fetching content-type
    try:
        content_type = event["headers"]["Content-Type"]
    except:
        content_type = event["headers"]["content-type"]
    # concate Content-Type: with content_type from event
    ct = "Content-Type: " + content_type + "\n"
# parsing message from bytes
    msg = email.message_from_bytes(ct.encode() + post_data)
# checking if the message is multipart
    print("Multipart check : ", msg.is_multipart())
# if message is multipart
    if msg.is_multipart():
        multipart_content = {}
        # retrieving form-data
        for part in msg.get_payload():
            # checking if filename exist as a part of content-disposition header
            if part.get_filename():
                # fetching the filename
                file_name = part.get_filename()
            multipart_content[
                part.get_param("name", header="content-disposition")
            ] = part.get_payload(decode=True)
# filename from form-data
        #file_name = json.loads(multipart_content["Metadata"])["filename"]
        # u uploading file to S3
        s3_upload = s3.put_object(
            Bucket="sanvalero-static-webs", Key=file_name, Body=multipart_content["file"]
        )
        
        #Send email to HR
        topic_arn = 'arn:aws:sns:eu-west-1:333984217794:S3-CV-SNS'
        message = 'Una solicitud de trabajo se ha enviado. Por favor revisa el C.V. en el bucket.'
        client.publish(TopicArn=topic_arn,Message=message)
# on upload success
        return {"statusCode": 200, "body": json.dumps("Gracias por su interes. Nos pondremos en contacto con usted lo antes posible.")}
    else:
        # on upload failure
        return {"statusCode": 500, "body": json.dumps("Upload failed!")}