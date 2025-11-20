#!/bin/bash
set -e

yum update -y

yum install -y httpd

INSTANCE_ID=$(ec2-metadata --instance-id | cut -d " " -f 2)
AVAILABILITY_ZONE=$(ec2-metadata --availability-zone | cut -d " " -f 2)
PRIVATE_IP=$(ec2-metadata --local-ipv4 | cut -d " " -f 2)

cat > /var/www/html/index.html << EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TechCorp Web Server</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            padding: 50px;
            border-radius: 20px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            backdrop-filter: blur(4px);
            border: 1px solid rgba(255, 255, 255, 0.18);
        }
        h1 {
            font-size: 3em;
            margin-bottom: 20px;
        }
        .info {
            font-size: 1.2em;
            margin: 10px 0;
        }
        .badge {
            display: inline-block;
            background: rgba(255, 255, 255, 0.2);
            padding: 10px 20px;
            border-radius: 10px;
            margin: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1> TechCorp Web Server</h1>
        <div class="info">
            <div class="badge">
                <strong>Instance ID:</strong> $INSTANCE_ID
            </div>
        </div>
        <div class="info">
            <div class="badge">
                <strong>Availability Zone:</strong> $AVAILABILITY_ZONE
            </div>
        </div>
        <div class="info">
            <div class="badge">
                <strong>Private IP:</strong> $PRIVATE_IP
            </div>
        </div>
        <p style="margin-top: 30px;"> Apache HTTP Server is running successfully!</p>
    </div>
</body>
</html>
EOF


systemctl start httpd
systemctl enable httpd
