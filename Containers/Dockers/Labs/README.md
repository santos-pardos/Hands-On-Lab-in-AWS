
# Basics Dockers and Dockerfile example. (not in Cloud9)

sudo su 

yum -y install docker 

systemctl start docker


# Netflix

https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Netflix.zip

FROM php:7.0-apache

COPY . /var/www/html/

EXPOSE 80

# 2048

https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/code/2048.zip    

FROM nginx:latest

COPY . /usr/share/nginx/html

EXPOSE 80


# Upload to ECR

Validation in AWS

AWS Configure  (Academy credentials)

Validation in ECR

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin xxxxxxx.dkr.ecr.us-east-1.amazonaws.com

docker tag 2048:latest xxxxx.dkr.ecr.us-east-1.amazonaws.com/dockers-unir:2048

docker push  xxxxx.dkr.ecr.us-east-1.amazonaws.com/dockers-unir:2048


# Docker Guides

https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Labs/Docker_Guides.zip

# Docker Examples (html, go, ruby, java, nodejs, python)

https://github.com/santos-pardos/Hands-On-Lab-in-AWS/tree/main/Containers/Dockers


#  Linux AMI - Dockers

https://docs.aws.amazon.com/es_es/AmazonECS/latest/developerguide/create-container-image.html
