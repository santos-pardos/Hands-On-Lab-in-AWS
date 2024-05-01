# Serverless Website on AWS
```
https://medium.com/@venkatagiri.sasanapuri/serverless-web-application-in-aws-703afb83b8ac
```
![](serverless.png)

## S3 Policy
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::<your-bucket>/*"
        }
    ]
}
```

## S3 CORS
```
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "POST"
        ],
        "AllowedOrigins": [
            "your-static-website-url"
        ],
        "ExposeHeaders": []
    }
]
```
