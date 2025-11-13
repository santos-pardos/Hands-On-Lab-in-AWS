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
wget  https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Ebook-Online.zip
unzip Ebook-Online.zip

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


