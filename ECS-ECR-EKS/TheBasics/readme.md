# Basics Dockers and Dockerfile example

sudo su 

yum -y install docker 

systemctl start docker


# Two Apps
wget https://sanvalero-static-webs.s3.eu-west-1.amazonaws.com/Drink-Water.zip 

unzip Drink-Water.zip 

rm Drink-Water.zip 

OR

wget https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/2048.zip

unzip 2048.zip.zip 

rm 2048.zip.zip 


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
