Linux AMI 2

#!/bin/bash
# Use this for your user data (script from top to bottom)
# install httpd (Linux 2 version)
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello World from $(hostname -f)</h1>" > /var/www/html/index.html

#!/bin/bash
sudo su
yum update -y
yum install -y httpd
cd /var/www/html
wget https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/jupiter-website.zip
unzip jupiter-website.zip)
cp -r jupiter-main/* /var/www/html/
rm -rf jupiter-main main.zip
systemctl enable httpd 
systemctl start httpd

#!/bin/bash -ex
# Updated to use Amazon Linux 2023
dnf -y update
dnf -y install httpd php php-fpm php-mysqli mariadb105
/usr/bin/systemctl enable httpd
/usr/bin/systemctl enable php-fpm
/usr/bin/systemctl start httpd
/usr/bin/systemctl start php-fpm
cd /var/www/html
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RSDBAS-3-124627/160-lab-DF-database-server/s3/lab-app-php7.zip
unzip lab-app-php7.zip -d /var/www/html/
chown apache:root /var/www/html/rds.conf.php

#!/bin/bash
yum update -y
yum install httpd -y
systemctl start httpd
systemctl enable httpd
cd /var/www/html
wget https://sanvalero-static-webs.s3.eu-west-1.amazonaws.com/breakout.zip
unzip breakout.zip


UBUNTU

#!/bin/bash
sudo apt update -y
sudo apt install -y apache2
sudo systemctl start apache2
sudo systemctl enable apache2
echo "<h1>This message is from : $(hostname -i)</h1>"> /var/www/html/index.html



Linux AMI 2023

#!/bin/bash
dnf update -y
dnf install nginx -y
systemctl start nginx
systemctl enable nginx
systemctl status nginx
cd /usr/share/nginx/html
rm index.html
wget https://sanvalero-static-webs.s3.eu-west-1.amazonaws.com/breakout.zip
unzip breakout.zip

#!/bin/bash
dnf install -y httpd git
cd /tmp
git clone --depth 1 --filter=blob:none --sparse https://github.com/santos-pardos/website-templates.git
cd website-templates
git sparse-checkout set coffee-shop-free-html5-template
cp -r coffee-shop-free-html5-template/* /var/www/html/
TOKEN=$(curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
ID=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/instance-id)
AZ=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/placement/availability-zone)
echo "<h1>La Ficha: te atiende el servidor $ID en la zona $AZ</h1>" > /var/www/html/servidor.html
systemctl enable --now httpd


#!/bin/bash
dnf update -y
dnf install nginx -y
systemctl start nginx
systemctl enable nginx
systemctl status nginx
cd /usr/share/nginx/html
rm index.html
https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Web-CV.zip
unzip Web-CV.zip

#!/bin/bash
#Install Apache Web Server and PHP
yum install -y httpd mysql php
#Download Lab files
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RESTRT-1/267-lab-NF-build-vpc-web-server/s3/lab-app.zip
unzip lab-app.zip -d /var/www/html/
#Turn on web server
chkconfig httpd on
service httpd start

#!/bin/bash
# Turn on password authentication for lab challenge
echo 'lab-password' | passwd ec2-user --stdin
sed -i 's|[#]*PasswordAuthentication no|PasswordAuthentication yes|g' /etc/ssh/sshd_config
systemctl restart sshd.service

#!/bin/bash
dnf update -y
dnf install nginx -y
systemctl start nginx
systemctl enable nginx
cd /usr/share/nginx/html
rm index.html
wget  https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Netflix.zip
unzip Netflix.zip

#!/bin/bash
dnf update -y
dnf install nginx -y
systemctl start nginx
systemctl enable nginx
cd /usr/share/nginx/html
rm index.html
wget  https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Ebook.zip
unzip Ebook.zip

#!/bin/bash 
dnf update -y 
dnf install -y docker 
service docker start 
systemctl enable docker.service
docker pull santospardos/upc:juiceshop
docker run -d -p 80:3000 santospardos/upc:juiceshop

#!/bin/bash
dnf update -y
dnf install httpd -y
systemctl start httpd
systemctl enable httpd
echo "Microservicio 1 desde $(hostname -f)" > /var/www/html/index.html

#!/bin/bash
sudo su
export DEBIAN_FRONTEND=non-interactive
apt-get update && apt-get upgrade -y
apt-get install apache2 git -y
systemctl enable apache2
systemctl start apache2
cd ..
cd ..
cd var
cd www
git clone https://github.com/samcolon/LUITProject19.git
cp -R /var/www/LUITProject19/HolidayGiftsWebsite/* /var/www/html/




