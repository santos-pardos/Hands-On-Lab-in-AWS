https://aws.amazon.com/es/getting-started/hands-on/deploy-wordpress-with-amazon-rds/

# 1. Install EC2

# 2. Install RDS
	Instance Name: wordpress
	First Database: wordpress (additionals settings)

# 3. Configuration 

----------------------New User in database: 

sudo yum install -y mysql

export MYSQL_HOST= your-endpoint
	
mysql -h wordpress.crmvoqdjozf6.us-east-1.rds.amazonaws.com -P 3306 -u admin -p
	
CREATE USER 'wordpress' IDENTIFIED BY 'wordpress-pass';
	
GRANT ALL PRIVILEGES ON wordpress.* TO wordpress;
	
FLUSH PRIVILEGES;
	
Exit
	
	
-----------------------Apache
	
sudo yum install -y httpd
	
sudo service httpd start

------------------------Wordpress
	
wget https://wordpress.org/latest.tar.gz
	
tar -xzf latest.tar.gz
	
$ ls
	
latest.tar.gz  wordpress
	
cd wordpress
	
cp wp-config-sample.php wp-config.php
	
vim wp-config.php

	
	
----------------------------Change de data in this section:

// ** MySQL settings - You can get this info from your web host ** //
	
/** The name of the database for WordPress */
	
define( 'DB_NAME', 'database_name_here' );

/** MySQL database username */
	
define( 'DB_USER', 'username_here' );

/** MySQL database password */
	
define( 'DB_PASSWORD', 'password_here' );

/** MySQL hostname */
	
define( 'DB_HOST', 'localhost' );




-----------------Change the define in the file for the define keys generate in this link:
	
-----------------https://api.wordpress.org/secret-key/1.1/salt/


define( 'AUTH_KEY',         'put your unique phrase here' );
	
define( 'SECURE_AUTH_KEY',  'put your unique phrase here' );
	
define( 'LOGGED_IN_KEY',    'put your unique phrase here' );
	
define( 'NONCE_KEY',        'put your unique phrase here' );
	
define( 'AUTH_SALT',        'put your unique phrase here' );
	
define( 'SECURE_AUTH_SALT', 'put your unique phrase here' );
	
define( 'LOGGED_IN_SALT',   'put your unique phrase here' );
	
define( 'NONCE_SALT',       'put your unique phrase here' );


# 4. Config Wordpress
	
sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
	
cd /home/ec2-user
	
sudo cp -r wordpress/* /var/www/html/
	
sudo service httpd restart
	
Open the public IP of the EC2 to start Wordpress
	
