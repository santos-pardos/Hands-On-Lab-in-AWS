## RDS - App AWS
```
RDS:  MySQL - Username: main -  Master password: lab-password  -  Initial database name: lab
```
## User-Data - App AWS
```
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
```



