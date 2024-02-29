# Install Software Ami Linux 2023
```
sudo dnf install wget php-mysqlnd httpd php-fpm php-mysqli mariadb105-server php-json php php-devel -y
```

# MySQL Config 
```
mysql -h wordpress.xxxxxxxxxx.us-east-1.rds.amazonaws.com -P 3306 -u admin -p
```
```
CREATE USER 'wordpress' IDENTIFIED BY 'wordpress-pass';
GRANT ALL PRIVILEGES ON wordpress.* TO wordpress;
FLUSH PRIVILEGES;
Exit
```
# Download Wordpress
```
wget https://wordpress.org/latest.tar.gz
tar -xzf latest.tar.gz
```
# Ec2-user Permissions
```
sudo usermod -a -G apache ec2-user
exit (salir y entrar en la consola de ec2)
groups 
sudo chown -R ec2-user:apache /var/www
```
# Final Installation
```
cd /home/ec2-user
sudo cp -r wordpress/* /var/www/html/
sudo chown -R apache:apache /var/www/html
sudo service httpd restart
sudo systemctl restart php-fpm
```
#  EIP
```
Coger una EIP y asignarla a la EC2
```
# DNS
```
http://dns-exit.com
Pedir dominio gratuito xxxx.work.gd
Pedir certificado wildcart o www
```
# ACM
```
Importar el certificado de Dns-exit en ACM (AWS Academy)
```
# ALB
```
TG la EC2
ALB con el certificado de ACM y puerto 443.
https://medium.com/@bjnandi/add-ssl-tls-from-aws-certificate-manager-acm-to-a-custom-google-domain-9e0dddae84ac
```
# Nombre final DNS
```
Crear un ALIAS (CNAME) en dns-exit.com con el valor del ALB
```
# Wordpress Initial Config
```
https://alb-dns/
ó
https://www.profesantos.word.gd
```
# wp-config.php
```
define( 'WP_HOME', 'http://elastic-ip' );
define( 'WP_SITEURL', 'http://elastic-ip' );
```

# Video
```
https://www.youtube.com/watch?v=oAWmSdqStcc&list=PLr35b7rSarzizDIWK4eKyl6mY4V_HxERi&index=118
```
# Lets Encrypt
```
sudo dnf install certbot python3-certbot-apache
sudo vim /etc/httpd/conf.d/wordpress.restocsv.es
         <VirtualHost *:80>
          ServerName wordpress.retocsv.es
          <Directory "/var/www/html/">
              Options None
              AllowOverride None
              ForceType text/plain
          </Directory>
        
          # ... remaining configuration
        RewriteEngine on
        </VirtualHost>

Alias en Route 53 -                  

sudo certbot --apache

sudo certbot delete
```
