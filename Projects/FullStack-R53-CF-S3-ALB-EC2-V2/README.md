# Challenge: Full Stack -(Route 53 - Cloudfront - ACM - S3 - ALB - EC2)


![](images/Cloudfront.png)

## S3
```
https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/cv.zip
```
```

{
    "Version": "2008-10-17",
    "Id": "Policy",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::your-bucket/*"
        }
    ]
}
```
```
Install a Static Website with S3
You can follow this video: 
https://youtu.be/xXCnaMxWUDk
```

## Cloudfront 

Change the xxxx for the right value
```
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
            "Resource": "arn:aws:s3:::xxxxxxxxxxxx/*",
            "Condition": {
                "StringEquals": {
                    "AWS:SourceArn": "arn:aws:cloudfront::xxxxxxxxx:distribution/xxxxxxxxxxx"
                }
            }
        }
    ]
}
```

## EC2
Create 1 SG - Port 80 (Web and ALB)

```
#!/bin/bash 
dnf update -y 
dnf install -y docker 
service docker start 
systemctl enable docker.service
docker pull santospardos/upc:juiceshop
docker run -d -p 80:3000 santospardos/upc:juiceshop
```

# Video
```
https://youtu.be/4bxVDFwqd5o
```


