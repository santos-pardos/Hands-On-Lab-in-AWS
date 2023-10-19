## Docker Install

```
sudo dnf update -y
sudo dnf install docker -y 
sudo systemctl start docker
sudo systemctl enable docker
docker –version
sudo systemctl status docker
sudo usermod -a -G docker ec2-user
newgrp docker
docker ps
docker run hello-world 
```

## Docker Compose Install

```
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose version
```
https://github.com/Haxxnet/Compose-Examples/tree/main/examples



## 2048

```
wget https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/code/2048.zip
FROM nginx:latest
COPY . /usr/share/nginx/html
EXPOSE 80

docker build -t mijuego2048 .
```


## Getting Started

```
git clone https://github.com/docker/getting-started-app.git
cd /
touch Dockerfile
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000

docker build -t getting-started .
docker run -dp 3000:3000 getting-started
docker ps
```

## Docker Hub

```
docker tag mariadb:10.11 santospardos/unir:mariadb
docker push santospardos/unir:mariadb
```

## Links
```
https://cloudkatha.com/how-to-install-docker-on-amazon-linux-2023/?utm_content=cmp-true
https://docs.docker.com/get-started/
https://github.com/docker/getting-started-app/tree/main
https://docs.docker.com/get-started/02_our_app/
https://github.com/docker/getting-started-app.git
```


