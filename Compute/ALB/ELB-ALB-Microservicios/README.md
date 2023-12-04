## Crea dos microservicios web

#!/bin/bash
dnf update -y
dnf install httpd -y
systemctl start httpd
systemctl enable httpd
cd /var/www/html
mkdir m1
echo "Microservicio 1 desde $(hostname -f)" > /var/www/html/m1/index.html
mkdir m2
echo "Microservicio 2 desde $(hostname -f)" > /var/www/html/m2/index.html