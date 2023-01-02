# Basics Dockers and Dockerfile example

sudo su 

yum -y install docker 

systemctl start docker


# Two Apps
wget https://sanvalero-static-webs.s3.eu-west-1.amazonaws.com/Drink-Water.zip 

unzip Drink-Water.zip 

rm Drink-Water.zip 

vim Dockerfile 

FROM php:7.0-apache 

COPY . /var/www/html/ 

EXPOSE 80 

docker build -t myapache . 

docker images 

docker run -d -p 80:80 myapache 

docker ps 

docker run -d -p 81:80 --name drinkwater myapache 

curl localhost

# OR

wget https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/code/2048.zip

unzip 2048.zip.zip 

rm 2048.zip.zip 

vim Dockerfile 

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

