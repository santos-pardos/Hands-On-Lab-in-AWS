#!/bin/bash
yum update -y
yum install httpd -y
systemctl start httpd
systemctl enable httpd
cd /var/www/html
wget https://sanvalero-static-webs.s3.eu-west-1.amazonaws.com/breakout.zip
unzip breakout.zip