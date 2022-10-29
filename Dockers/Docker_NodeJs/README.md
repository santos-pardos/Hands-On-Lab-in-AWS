# Docker NodeJS

# Install Cloud9

If you use AWS Cloud9. You have docker, node, npm, git , python installed

If you use LINUX AMI 2

$ sudo yum install -y gcc-c++ make 

$ curl -sL https://rpm.nodesource.com/setup_16.x | sudo -E bash -

$ sudo yum install -y nodejs 

$ sudo yum install -y git

$ sudo yum intall -y python

# Test the NodeJS Server

Upload the file: check_server.js

$ node --inspect check server.js 

http://myPublicIP:3000/

# Docker the NodeJS App

$ sudo mkdir expapp

$ npm init -y

Review the package.json file

Add the express extension

$ sudo npm install express --save

$ node app.js

http://myPublicIP:3002/



