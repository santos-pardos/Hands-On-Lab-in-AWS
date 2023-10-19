## EC2
```
#!/bin/bash -ex
yum -y update
yum -y install httpd php mysql php-mysql
chkconfig httpd on
service httpd start
cd /var/www/html
wget https://us-west-2-aws-training.s3.amazonaws.com/courses/spl-13/v4.2.27.prod-f0f1d0c2/scripts/app.tgz
tar xvfz app.tgz
chown apache:root /var/www/html/rds.conf.php
```

## RDS
```
DB instance identifier: myDB
Master username: admin
Master password: lab-password
Confirm password:lab-password

Initial database name: myDB
```