## User Data for AMI Linux 2023 - Juice Shop

```
#!/bin/bash 
sudo dnf update -y 
sudo dnf install -y docker 
service docker start 
systemctl enable docker.service
docker pull santospardos/upc:juiceshop
docker run -d -p 80:3000 santospardos/upc:juiceshop
```

## User Data for AMI Linux 2023 - Neflix

```
#!/bin/bash 
sudo dnf update -y 
sudo dnf install -y docker 
service docker start 
systemctl enable docker.service
docker pull santospardos/upc:netflix
docker run -d -p 80:80 santospardos/upc:netflix
```

## User Data for AMI Linux 2023 - Cafetería

```
#!/bin/bash
dnf update -y
dnf install nginx -y
systemctl start nginx
systemctl enable nginx
cd /usr/share/nginx/html
rm index.html
wget https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Cafeteria.zip
unzip Cafeteria.zip
```
