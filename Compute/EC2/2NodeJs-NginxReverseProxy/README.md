## Install Nodejs
```
sudo apt update
sudo apt upgrade -y
sudo apt install nodejs
node --version
sudo apt install npm
mkdir mynodeapp && cd mynodeapp
npm init -y
npm i express

vim app.js

const express = require("express"); 
const app = express(); // Initializing Express App

// Sending Hello World when anyone browse your webpage

app.get("/*", (req, res)=>{
        res.send('Hello World'); 
});

app.listen(3000, ()=> console.log("App Listening on port 3000"));

node app.js


vim app2.js

const express = require("express"); 
const app = express(); // Initializing Express App

// Sending Hello World when anyone browse your webpage

app.get("/*", (req, res)=>{
        res.send('Hello World'); 
});

app.listen(4000, ()=> console.log("App Listening on port 4000"));

node app2.js
```

## Install PM2
```
sudo npm install -g pm2
pm2 start app.js
pm2 status
pm2 stop (app/id)
pm2 restart (app/id)
curl localhost:3000
```
## Option A Install Nginx Reverse Proxy
```
sudo apt install nginx
systemctl status nginx
systemctl enable nginx
cd /etc/nginx/conf.d
sudo nano configuration.conf

server {
server_name 34.241.81.252;
location /hello {
        proxy_pass http://127.0.0.1:3000;
      }
location /hello2 {
        proxy_pass http://127.0.0.1:4000;
      }
}

sudo nginx -t
sudo service nginx restart
```

## Option B Install Nginx Reverse Proxy
sudo vim /etc/nginx/sites-available/default.conf

server {
server_name 34.241.81.252;
location /hello {
        proxy_pass http://127.0.0.1:3000;
      }
location /hello2 {
        proxy_pass http://127.0.0.1:4000;
      }
}
