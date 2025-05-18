# Visual Studio Code Webserver URL
```
https://vscode.dev/tunnel/vscode-demo-tunnel
```

# Install Docker in AMI Linux 2023 (Fedora)
```
sudo dnf install docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
newgrp docker
```

Install Docker extension
```
ls -l /var/run/docker.sock
sudo chmod 666 /var/run/docker.sock
sudo systemctl restart docker.service
```

# Install Docker-Compose
```
sudo curl -s https://api.github.com/repos/docker/compose/releases/latest | grep browser_download_url | grep docker-compose-linux-x86_64 | cut -d '"' -f 4 | wget -qi -
```
```
sudo chmod +x docker-compose-linux-x86_64
```
```
sudo mv docker-compose-linux-x86_64 /usr/local/bin/docker-compose
```
```
docker-compose --version
```

# Netflix

https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Netflix.zip

FROM php:7.0-apache

COPY . /var/www/html/

EXPOSE 80

# 2048
```
https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/code/2048.zip    
```
```
FROM nginx:latest
COPY . /usr/share/nginx/html
EXPOSE 80
```
```
FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install -y nginx zip curl
RUN echo "daemon off;">>/etc/nginx/nginx.conf
RUN curl -o /var/www/html/master.zip -L https://codeload.github.com/gabrielecirulli/2048/zip/master
RUN cd /var/www/html/ && unzip master.zip && mv 2048-master/* . && rm -rf 2048-master master.zip
EXPOSE 80
CMD ["/usr/sbin/nginx", "-c", "/etc/nginx/nginx.conf"]
```

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
