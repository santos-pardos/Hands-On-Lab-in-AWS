## Install Linux and Apache

sudo dnf install httpd -y

sudo systemctl start httpd

sudo systemctl enable httpd

curl localhost

http://public ip/


## EFS system

cd /var/www/html

mkdir efs

sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-0f2512d76577aa529.efs.us-east-1.amazonaws.com:/ efs

(you can read this command in Attach options in EFS service into AWS)

df -h

## Change the root directory

sudo nano /etc/httpd/conf/httpd.conf

change DocumentRoot "/var/www/html"  to DocumentRoot "/var/www/html/efs"

sudo systemctl restart httpd

(sudo service httpd restart)

cd /var/www/html/efs

copy a html website o write one small html code.

visit the Public IP to see the website


## Links

https://www.tecmint.com/change-root-directory-of-apache-web-server/

