## LAMP Linux AMI 2 (Centos)
```
sudo yum update -y
sudo yum install -y httpd24 php72 mysql57-server php72-mysqlnd
cat /etc/system-release
sudo service httpd start
sudo service httpd start
sudo chkconfig httpd on
chkconfig --list httpd
ls -l /var/www
sudo usermod -a -G apache ec2-user
exit
groups
sudo chown -R ec2-user:apache /var/www
sudo chmod 2775 /var/www
find /var/www -type d -exec sudo chmod 2775 {} \;
find /var/www -type f -exec sudo chmod 0664 {} \;
echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php
http://my.public.dns.amazonaws.com/phpinfo.php
```

## LAMP Ubuntu

### Apache
```
sudo apt update
sudo apt upgrade -y
sudo apt install apache2
sudo systemctl enable apache2
sudo systemctl status apache2
```

### MySQL
```
sudo apt install mysql-server -y
sudo mysql
sudo mysql_secure_installation
sudo mysql -p
```

### PHP
```
sudo apt install php libapache2-mod-php php-mysql
php -v


### CREATE VIRTUAL HOST
sudo mkdir /var/www/projectlamp
sudo chown -R $USER:$USER /var/www/projectlamp
sudo vi /etc/apache2/sites-available/projectlamp.conf

<VirtualHost *:80>
    ServerName projectlamp
    ServerAlias www.projectlamp 
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/projectlamp
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

sudo ls /etc/apache2/sites-available/
sudo a2ensite projectlamp.conf
sudo a2dissite 000-default
sudo apache2ctl configtest
sudo systemctl restart apache2
sudo vi /etc/apache2/mods-enabled/dir.conf

<IfModule mod_dir.c>
    #Change this:
    #DirectoryIndex index.html index.cgi index.pl index.php index.xhtml index.htm
    #To this:
    DirectoryIndex index.php index.html index.cgi index.pl index.xhtml index.htm
</IfModule>

sudo systemctl reload apache2
vim /var/www/projectlamp/index.php

<?php
phpinfo();

sudo rm /var/www/projectlamp/index.php
```

### Links
```
https://dev.to/mannyuncharted/web-stack-implementation-lamp-stack-in-aws-11j0
https://dev.to/mannyuncharted/mean-stack-implementation-on-an-aws-ec2-instance-4gec
https://dev.to/mannyuncharted/web-stack-implementation-lamp-stack-in-aws-11j0
https://dev.to/mannyuncharted/mean-stack-implementation-on-an-aws-ec2-instance-4gec
https://dev.to/mannyuncharted/mean-stack-implementation-on-an-aws-ec2-instance-4gec
https://blog.devgenius.io/deploy-your-mean-app-on-aws-ec2-a24fe3c2073f
https://medium.com/@deepuaugust/deploying-a-mean-mern-stack-application-to-an-aws-ec2-instance-d8828f4f02e2
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html
https://dev.to/abdulwaqar844/how-to-build-and-deploy-a-mernreactexpressmongodbnodejs-stack-application-on-aws-ec2-3e93
https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server
https://www.knowledgehut.com/blog/web-development/install-nodejs-on-ubuntu
https://www.digitalocean.com/community/tutorials/install-tomcat-9-ubuntu-1804
```
