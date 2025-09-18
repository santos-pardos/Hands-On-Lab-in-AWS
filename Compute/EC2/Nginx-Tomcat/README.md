### Linux Ami 2023
```
sudo dnf update
sudo dnf install java
java -version
sudo dnf -y install wget
wget https://archive.apache.org/dist/tomcat/tomcat-10/v10.0.23/bin/apache-tomcat-10.0.23.tar.gz
tar -xvf apache-tomcat-10*.tar.gz
sudo mv apache-tomcat-10.0.23 /usr/local/tomcat
cd /usr/local/tomcat/bin
./startup.sh
```
```
sudo dnf install nginx -y
sudo systemctl enable nginx
sudo systemctl start nginx
sudo systemctl status nginx
```
```
vi /etc/nginx/nginx.conf
```
```
 server {
        listen       80;
        listen       [::]:80;
        server_name  ec2-44-203-73-141.compute-1.amazonaws.com; # Change the DNS name

        location / {
        proxy_pass http://localhost:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;

        }
    }
```

```
sudo nginx -t
sudo systemctl restart nginx
```



