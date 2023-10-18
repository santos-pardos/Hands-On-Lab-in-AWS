## Install NodeJs
```
sudo apt update
sudo apt -y upgrade
sudo apt install nodejs
sudo apt install npm
nodejs -v && npm --version
```

## Web Server
```
sudo nano index.js

const express = require('express'); 
const app = express(); 
[Text Wrapping Break] 
app.get('/', function (req, res) { 
  res.send('Hello World!'); 
}); 
app.listen(3000, function () { 
  console.log('Example app listening on port 3000!'); 
}); 

node index.js

sudo nano idex2.js

function add(y,z) { 
  return y+z; 
} 
console.log(add(81, 9)) 

node index2.js
```

## Remove Nodejs
```
sudo apt remove nodejs
sudo apt purge nodejs -y
npm current
npm deactivate
```

## Installa Python
```
sudo apt update
sudo apt -y upgrade
python3 -V
sudo apt install -y python3-pip
pip3 install numpy
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
sudo apt install -y python3-venv
mkdir environments
cd environments
python3 -m venv my_env
ls my_env
source my_env/bin/activate
nano hello.py
print("Hello, World!")
python hello.py
deactivate
```
## Install .NET
```
sudo dnf install dotnet-sdk-7.0
sudo dnf install aspnetcore-runtime-7.0
dotnet new console -o App -n DotNet.Docker
cd App
dotnet run
```

## Install Nodejs Game (Just in case you know Dockers)
```
sudo mkdir phaserquest
cd phaserquest
sudo wget https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/phaserquest-master.zip
sudo unzip phaserquest-master.zip
docker-compose build
docker-compose up -d
```

## Links
```
https://www.knowledgehut.com/blog/web-development/install-nodejs-on-ubuntu#how-to-uninstall%C2%A0node.js%C2%A0from-ubuntu?%C2%A0
https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server
https://github.com/Jerenaux/phaserquest
https://learn.microsoft.com/es-es/dotnet/core/docker/build-container?tabs=windows
https://dotnet.microsoft.com/es-es/download/dotnet/7.0

```
