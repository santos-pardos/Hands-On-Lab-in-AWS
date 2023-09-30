## Netflix

#!/bin/bash

$ dnf update -y

dnf install nginx -y

systemctl start nginx

systemctl enable nginx

cd /usr/share/nginx/html

rm index.html

wget https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Netflix.zip

unzip Netflix.zip



## Nc.me (we need GitHub education account)

Buy the domain.me

Create public zone in Route 53

Change de NS in namecheap.me

Create a Record netflix.profesantos.me in Route 53 with the Public IP of Nginx


## Free domain

https://dnsexit.com/

Get a free domain word.gd but you CANT redirect the DNS to AWS Route 53

Create a record with the public IP aws ec2 machine.



## Change the Nginx Config (if you are going to install SSL, otherwise not)

sudo nano /etc/nginx/nginx.conf

(find server_name _;)

server {

        listen       80;

        listen       [::]:80;

        server_name  netflix.profesantos.me;

sudo systemctl restart nginx
sudo nginx -t

## Install Certbot

sudo python3 -m venv /opt/certbot/

sudo /opt/certbot/bin/pip install --upgrade pip

sudo /opt/certbot/bin/pip install certbot certbot-nginx

sudo ln -s /opt/certbot/bin/certbot /usr/bin/certbot

sudo certbot --nginx


### Links

https://dev.to/0xfedev/how-to-install-nginx-as-reverse-proxy-and-configure-certbot-on-amazon-linux-2023-2cc9

https://nc.me

https://namecheap.com
