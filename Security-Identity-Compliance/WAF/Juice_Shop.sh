#!/bin/bash 
yum update -y 
yum install -y docker 
service docker start 
systemctl enable docker.service
docker pull bkimminich/juice-shop 
docker run -d -p 80:3000 bkimminich/juice-shop