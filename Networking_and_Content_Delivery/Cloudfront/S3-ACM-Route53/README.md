## Web
```
https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Web-CV.zip

Bucket Policy:
{
    "Version": "2008-10-17",
    "Id": "PolicyForCloudFrontPrivateContent",
    "Statement": [
        {
            "Sid": "AllowCloudFrontServicePrincipal",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudfront.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*",
            "Condition": {
                "StringEquals": {
                    "AWS:SourceArn": "arn:aws:cloudfront::xxxxxxxxxxxxxx:distribution/xxxxxxxxxx"
                }
            }
        }
    ]
}
```
## Links
```
https://medium.com/@taiwolateef55/hosting-a-static-website-on-aws-using-amazon-s3-cloudfront-route53-and-acm-ddfc755b7038
```
