# Serverless Website on AWS

![](serverless.png)

## steps
```
Create Lambda Function:  ProcessContactForm
  NodeJs 18
  Import Lambda.zip
  Use the Test Event JSON
Create REST API Public: ContactFormApl
  Create Resource: Submit
  Create Method: Post
  Deploy API
Create DynamoDB: ContactFormEntries
  SubmissionId - String
Change in de Website file script.js
  fetch('your-api-gateway-url', {    (change your URL API GW)
Upload Website to the S3
Change the S3 options to set up a website
Configure CORS in API GW (options CORS)
Add the CORS json file in S3 CORS options
```

## Website
```
https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Severless/Website-Form/website.zip
```

## Lambda.zip
```
https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Severless/Website-Form/lambda.zip
```

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
## Test Lambda
```
{
  "name": "myname",
  "email": "mymail@example.com",
  "subject": "lambda-testing",
  "message": "A message from lambda"
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
            "*"
        ],
        "ExposeHeaders": []
    }
]
```

## Links
```
https://medium.com/@venkatagiri.sasanapuri/serverless-web-application-in-aws-703afb83b8ac
https://medium.com/cloud-native-daily/revolutionizing-web-development-creating-serverless-contact-forms-with-aws-8d2f2220329a
https://medium.com/better-programming/implementing-a-web-form-on-aws-with-bare-html-and-js-5b0a319a702e
```
