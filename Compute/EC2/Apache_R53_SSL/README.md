## Apache
```
sudo apt update
sudo apt upgrade
sudo apt install apache2
sudo systemctl start apache2
sudo systemctl enable apache2
```
## Firewall
```
sudo ufw allow http
sudo ufw allow https
sudo ufw allow OpenSSH
sudo ufw enable
```

## Website
```
sudo mkdir -p /var/www/html/myweb
sudo echo "Setting Up a Secure Apache Server on Ubuntu 24.04" > index.html
sudo cp index.html /var/www/html/myweb/index.html
sudo chown -R www-data:www-data /var/www/html/myweb/
```
## VirtualHost
```
sudo nano /etc/apache2/sites-available/myweb.conf

# Insert the following configuration:
<VirtualHost *:80>
    ServerAdmin admin@myweb.retocsv.es
    ServerName myweb.retocsv.es
    DocumentRoot /var/www/html/myweb
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

sudo a2ensite myweb
sudo a2dissite 000-default
sudo systemctl enable apache2
sudo systemctl restart apache2
```
## Test Website
```
wget myweb.retocsv.es
http://myweb.retocsv.es
```
## CertBot
```
sudo apt install certbot python3-certbot-apache
sudo certbot --apache

https://myweb.retocsv.es
```
## Link
https://linuxconfig.org/setting-up-a-secure-apache-server-on-ubuntu-24-04
