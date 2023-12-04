# RETO - Network Load Balancer y NodeJS


## Instalación NodeJs
```
sudo apt update
sudo apt upgrade -y
sudo apt install nodejs
sudo apt install npm
nodejs -v && npm --version
npm install express -y
```

## Aplicación pequeño Web Server en Nodejs
```
sudo nano index.js

const express = require('express'); 
const app = express(); 
app.get('/', function (req, res) { 
  res.send('Microservicio 1 - Hola Mundo!'); 
}); 
app.listen(3000, function () { 
  console.log('Ejemplo de aplicacion escuchando por el puerto 3000!'); 
}); 

node index.js

```

## Instalar un NLB con un TG por el puerto 3000


## Si quieres limpiar Nodejs
```
sudo apt remove nodejs
sudo apt purge nodejs -y
npm current
npm deactivate
```
