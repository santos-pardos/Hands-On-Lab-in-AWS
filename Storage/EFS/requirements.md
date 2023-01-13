# Requirements

SGWeb for EC2 (22 port) and  SGEfs for Efs (2049 port)

# Install User Data

#!/bin/bash

yum update -y

yum install httpd -y

systemctl start httpd

systemctl enable httpd

yum -y install nfs-utils

# Linux Commands

cd /var/www/html

mkdir efs-mount


# Mount folder

sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-09d8395cbf7d9bf1c.efs.us-east-1.amazonaws.com:/   efs-mount

# Neflix Website

wget https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Netflix.zip 

# Modify the Apache root document

/etc/httpd/conf/httpd.conf

DocumentRoot "/var/www/html/efs-mount"


# Clean Up

umount -a

----------------------------------------------------------------------------------------


# GUIA OFICIAL

https://docs.aws.amazon.com/es_es/efs/latest/ug/wt2-apache-web-server.html

#cloud-config
package_upgrade: true
packages:
- nfs-utils
- httpd
runcmd:
- echo "$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone).fs-09d8395cbf7d9bf1c.efs.us-east-1.amazonaws.com:/    /var/www/html/efs-mount-point   nfs4    defaults" >> /etc/fstab
- mkdir /var/www/html/efs-mount-point
- mount -a
- touch /var/www/html/efs-mount-point/test.html
- service httpd start
- chkconfig httpd on

# Other Links
https://cloudbytes.dev/aws-academy/mount-amazon-efs-drive-on-ec2-ubuntu-linux-using-nfs-utils

https://docs.aws.amazon.com/efs/latest/ug/wt1-getting-started.html

