# Docker NodeJS

# Install Cloud9

If you use AWS Cloud9. You have docker, node, npm, git , python installed
(when you enter in sudo su in cloud9 , you need to install nodejs to run npm with the root account)

If you use LINUX AMI 2

$ sudo su

yum install -y gcc-c++ make 

curl -sL https://rpm.nodesource.com/setup_16.x | sudo -E bash -

yum install -y nodejs 

sudo yum install -y git

sudo yum intall -y python

# Test the NodeJS Server

Upload the file: check_server.js

node --inspect check server.js 

http://myPublicIP:3000/

# Docker the NodeJS App

Create a folder with Cloud9, for example, Lab01

Upload app.js and Dockerfile
(you can create the files too)

npm init -y

Review the package.json file

Add the express extension

npm install express --save

Test the app

node app.js

http://myPublicIP:3002/

Create the image

docker build -t express-app .

docker images

Run the docker

docker run -p 3002:3002 express-app
