Linux AMI 2

 #!/bin/bash
yum update -y
yum install httpd -y
systemctl start httpd
systemctl enable httpd
cd /var/www/html
wget https://sanvalero-static-webs.s3.eu-west-1.amazonaws.com/breakout.zip
unzip breakout.zip


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
wget https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Netflix.zip
unzip Netflix.zip

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
apt-get update && apt-get upgrade -y
apt-get install apache2 git unzip wget -y
systemctl enable apache2
systemctl start apache2
cd /var/wwww/html
sudo rm index.html
sudo wget https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/HolidayGiftsWebsite.zip
sudo unzip HolidayGiftsWebsite.zip

