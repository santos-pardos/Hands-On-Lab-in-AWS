## Install user-data
```
#!/bin/bash
sudo su
yum update -y
yum install -y httpd
cd /var/www/html
wget [https://github.com/azeezsalu/jupiter/archive/refs/heads/main.zip](https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/jupiter-website.zip)
unzip jupiter-website.zip)
cp -r jupiter-main/* /var/www/html/
rm -rf jupiter-main main.zip
systemctl enable httpd 
systemctl start httpd
```
