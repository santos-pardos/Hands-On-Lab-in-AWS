## 2 APACHES with EFS System

## Install Linux and Apache
```
sudo dnf install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
curl localhost
http://public ip/
```

## EFS system
```
cd /var/www/html
mkdir efs
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-0f2512d76577aa529.efs.us-east-1.amazonaws.com:/ efs
(you can read this command in Attach options in EFS service into AWS)
df -h
```
## Change the root directory in apache
```
sudo nano /etc/httpd/conf/httpd.conf
change DocumentRoot "/var/www/html"  to DocumentRoot "/var/www/html/efs"
sudo systemctl restart httpd
cd /var/www/html/efs
sudo rm -f /etc/httpd/conf.d/welcome.conf
echo "<h1>Mi web desde el disco de 10GB</h1>" | sudo tee /var/www/html/efs/index.html
sudo chown -R apache:apache /var/www/html/efs
sudo chmod -R 755 /var/www/html/efs
sudo systemctl restart httpd
sudo httpd -S | grep "Main DocumentRoot"
```

## Links
```
https://www.tecmint.com/change-root-directory-of-apache-web-server/
```

