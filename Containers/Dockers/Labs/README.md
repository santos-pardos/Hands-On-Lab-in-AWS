# Visual Studio Code - Docker Extensions 
 Install Docker exension

```
sudo dnf install docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
newgrp docker
```


```
ls -l /var/run/docker.sock
sudo chmod 666 /var/run/docker.sock
sudo systemctl restart docker.service
```
# Install Docker (not in Cloud9)

sudo yum -y install docker 

sudo systemctl start docker

# Install Docker-Compose (yes in Cloud9)

sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose version

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

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin xxxxxxx.dkr.ecr.us-east-1.amazonaws.com

docker tag 2048:latest xxxxx.dkr.ecr.us-east-1.amazonaws.com/dockers-unir:2048

docker push  xxxxx.dkr.ecr.us-east-1.amazonaws.com/dockers-unir:2048


# Docker Guides

https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Labs/Docker_Guides.zip

# Docker Examples (html, go, ruby, java, nodejs, python)

https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Labs/Labs-Dockers/Labs.zip


#  Linux AMI - Dockers

https://docs.aws.amazon.com/es_es/AmazonECS/latest/developerguide/create-container-image.html
