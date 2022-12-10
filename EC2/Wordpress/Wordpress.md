Step-By-Step Instructions For Creating A WordPress Blog Running on An EC2 Instance in AWS

# 1. Install EC2

# 2. Configuration
STEP 1 — Configure the required environment variables

DBName='wordpress'

DBUser='wordpress'

DBPassword='Wordpr3ss-pass'

DBRootPassword='Wordpr3ss-pass'


STEP 2 — Install the required components

sudo yum install -y mariadb-server httpd wget

sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2

Wait until the installation finishes.

STEP 3 — Configure the web and database servers to run at startup

sudo systemctl enable httpd

sudo systemctl enable mariadb

sudo systemctl start httpd

sudo systemctl start mariadb


STEP 4 — Configure MariaDB Password

mysqladmin -u root password $DBRootPassword


STEP 5 — Install WordPress

sudo wget http://wordpress.org/latest.tar.gz -P /var/www/html

cd /var/www/html

sudo tar -zxvf latest.tar.gz

sudo cp -rvf wordpress/* .

sudo rm -R wordpress

sudo rm latest.tar.gz


STEP 6 — Configure WordPress

sudo cp ./wp-config-sample.php ./wp-config.php

sudo sed -i "s/'database_name_here'/'$DBName'/g" wp-config.php

sudo sed -i "s/'username_here'/'$DBUser'/g" wp-config.php

sudo sed -i "s/'password_here'/'$DBPassword'/g" wp-config.php   

sudo chown apache:apache * -R


STEP 7 Create the WordPress database

echo "CREATE DATABASE $DBName;" >> /tmp/db.setup

echo "CREATE USER '$DBUser'@'localhost' IDENTIFIED BY '$DBPassword';" >> /tmp/db.setup

echo "GRANT ALL ON $DBName.* TO '$DBUser'@'localhost';" >> /tmp/db.setup

echo "FLUSH PRIVILEGES;" >> /tmp/db.setup

mysql -u root --password=$DBRootPassword < /tmp/db.setup

sudo rm /tmp/db.setup

Next, we need to run the below command to find out the DNS name of the EC2 instance, so we can access our blog and finish configuring it:

curl http://169.254.169.254/latest/meta-data/public-hostname


# Config Wordpress
Open Public IP or DNS Name