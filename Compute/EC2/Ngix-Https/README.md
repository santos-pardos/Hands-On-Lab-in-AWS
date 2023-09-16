1. Install Ngix en Linux AMI 2023

sudo dnf install nginx -y

sudo systemctl start nginx 

sudo systemctl enable nginx

sudo systemctl status nginx

http://public_ip


2. Grab a certificate from  https://zerossl.com/

(90 days free @hotmail.com). You need to validate the subdomain certificate through email o DNS record

Download the certificate

Copy the zip file to the Linux AMI 2023


3. Install the certificate

sudo mkdir /etc/pki/nginx/

sudo mkdir /etc/pki/nginx/private

unzip csv.profesantos.zip

sudo cat certificate.crt ca_bundle.crt >> certificate.crt

sudo cp certificate.crt /etc/pki/nginx/

sudo cp private.crt /etc/pki/nginx/private/


4. Upload your website

cd /usr/share/nginx/html

sudo rm index.html

sudo wget https://sanvalero-static-webs.s3.eu-west-1.amazonaws.com/breakout.zip

sudo unzip breakout.zip


5. Change the SSL configuration in this file:

sudo cat /etc/nginx/nginx.conf

Remove the comments the SSL area

Find and change this 2 lines:

        ssl_certificate "/etc/pki/nginx/certificate.crt";

        ssl_certificate_key "/etc/pki/nginx/cprivate.key";

Change the line:

server_name _;   to       server_name migrupo.profesantos.cloud;



6. Restart Nginx. Change DNS. Visit the web

sudo systemctl restart nginx

Create a DNS registre EC2 Public IP ----  migrupo.profesantos.cloud

https: migrupo.profesantos.cloud


## Links
https://www.armanism.com/blog/install-free-ssl-on-nginx

https://zerossl.com/

https://geekflare.com/es/zerossl-apache-nginx/

https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-20-04

https://awswithatiq.com/ssl-setup-on-amazon-linux-2023-using-nginx-and-letsencrypt/

https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal

https://repost.aws/knowledge-center/ec2-linux-ubuntu-install-ssl-cert

https://docs.aws.amazon.com/es_es/efs/latest/ug/wt2-apache-web-server.html

