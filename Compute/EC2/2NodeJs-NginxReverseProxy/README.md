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
const app = express();

app.get("/", (req, res) => {
  res.send("Hola mundo con Express . Puerto 3000. 🚀");
});

app.listen(3000, () => {
  console.log("Servidor corriendo en http://localhost:3000");
});



node app.js


vim app2.js


const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("Hola mundo con Express . Puerto 4000.  🚀");
});

app.listen(4000, () => {
  console.log("Servidor corriendo en http://localhost:4000");
});




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
sudo nano /etc/nginx/nginx.conf
(pega el fichero del repositorio)



NOTE: Open SG port 80


