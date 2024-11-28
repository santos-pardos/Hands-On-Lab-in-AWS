#!/bin/bash

# variables
DB_NAME="wordpress_db"            # Name of the database
DB_USER="sriwp_dbuser"            # Database username
DB_PASSWORD="9867awsways@29"      # Database password

WORDPRESS_DIR="/var/www/html"     # wordpress code directory

# Update the system
yum update -y

# Install expect package
yum install expect -y

# Install Apache HTTP server
yum install -y httpd

# Start Apache
systemctl start httpd

# Enable Apache to start on boot
systemctl enable httpd

# Create a PHP info page
echo "<?php phpinfo(); ?>" > ${WORDPRESS_DIR}/index.php

# Enable PHP 7.4
amazon-linux-extras enable php7.4 -y

# Install required PHP modules
sudo yum install php php-{pear,cgi,common,curl,mbstring,gd,mysqlnd,gettext,bcmath,json,xml,fpm,intl,zip,imap} -y

# Install MariaDB
sudo yum install mariadb-server -y

# Start MariaDB
sudo systemctl start mariadb

# Enable MariaDB to start on boot
sudo systemctl enable mariadb

# Install 
yum install expect -y

# Secure the MariaDB installation
echo "Securing MariaDB installation..."
expect - <<EOF
spawn mysql_secure_installation
expect "Enter current password for root (enter for none):"
send "\r"
expect "Set root password?"
send "y\r"
expect "New password:"
send "$DB_PASSWORD\r"
expect "Re-enter new password:"
send "$DB_PASSWORD\r"
expect "Remove anonymous users?"
send "y\r"
expect "Disallow root login remotely?"
send "y\r"
expect "Remove test database and access to it?"
send "y\r"
expect "Reload privilege tables now?"
send "y\r"
expect eof
EOF
echo "MariaDB installation secured."

# Change to the user's home directory
cd /home/ec2-user

# Download the latest WordPress
wget https://wordpress.org/latest.zip

# Unzip the WordPress archive
unzip latest.zip

# Move WordPress files to Apache's web directory
mv wordpress/* ${WORDPRESS_DIR}

# Change ownership of the web directory
chown -R ec2-user:apache ${WORDPRESS_DIR}

# Create the WordPress database
mysql -u root -p$DB_PASSWORD -e "CREATE DATABASE $DB_NAME;"

# Create a user for the database
mysql -u root -p$DB_PASSWORD -e "CREATE USER '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASSWORD';"

# Grant privileges to the user
mysql -u root -p$DB_PASSWORD -e "GRANT ALL PRIVILEGES ON $DB_NAME.* TO '$DB_USER'@'localhost';"

# Flush privileges
mysql -u root -p$DB_PASSWORD -e "FLUSH PRIVILEGES;"

# Change to the WordPress directory
cd ${WORDPRESS_DIR}

# Create a WordPress configuration file from the sample
cp wp-config-sample.php wp-config.php

# Replace database name in the configuration file
sed -i "s/database_name_here/$DB_NAME/" wp-config.php

# Replace database username in the configuration file
sed -i "s/username_here/$DB_USER/" wp-config.php

# Replace database password in the configuration file
sed -i "s/password_here/$DB_PASSWORD/" wp-config.php

# Replace database host in the configuration file
sed -i "s/localhost/localhost/" wp-config.php


# Set appropriate permissions for the web directory (directories)
sudo find ${WORDPRESS_DIR} -type d -exec chmod 755 {} \;

# Set appropriate permissions for the web directory (files)
sudo find ${WORDPRESS_DIR} -type f -exec chmod 644 {} \;

# Restart Apache
sudo systemctl restart httpd

echo 
echo "**********************************************************"
echo "******** User data has been executed successfully ********"
echo "**********************************************************"
echo
