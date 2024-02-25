# Install Software Ami Linux 2023
```
sudo dnf install wget php-mysqlnd httpd php-fpm php-mysqli mariadb105-server php-json php php-devel -y
```
```
sudo dnf install wget php-mysqlnd httpd php-fpm php-mysqli php-json php php-devel -y
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
newgrp ec2-user
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
# Wordpress Initial Config
```
http://public-ip/
```
# wp-config.php
```
define( 'WP_HOME', 'http://elastic-ip' );
define( 'WP_SITEURL', 'http://elastic-ip' );
```

# Video
```
https://www.youtube.com/xxx
```
```
