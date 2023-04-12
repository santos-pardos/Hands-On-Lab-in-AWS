# Hands-On-Lab-in-AWS about containers and dockers

# Docker CE Install

sudo yum install docker -y

sudo service docker start

sudo usermod -a -G docker ec2-user

Make docker auto-start

sudo chkconfig docker on

Because you always need it....

sudo yum install -y git

Close the ssh session and enter again to execute docker with your user (ec2-user)

sudo systemctl status docker.service

# docker-compose install

## Option 1 (Linux AMI 2023)

sudo dnf -y install wget

sudo curl -s https://api.github.com/repos/docker/compose/releases/latest

sudo chmod +x docker-compose-linux-x86_64

sudo mv docker-compose-linux-x86_64 /usr/local/bin/docker-compose

docker-compose --version


## Option 2 (Linux AMI 2)
sudo yum install python3-pip

sudo pip3 install docker-compose

sudo systemctl enable docker.service

sudo systemctl start docker.service

## Option 3
Copy the appropriate docker-compose binary from GitHub:

sudo curl -L https://github.com/docker/compose/releases/download/1.3.1/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

Fix permissions after download:

sudo chmod +x /usr/local/bin/docker-compose

Verify success:

docker-compose version


# Other Links

https://www.cyberciti.biz/faq/how-to-install-docker-on-amazon-linux-2/

https://floatingcloud.io/how-to-install-docker-and-compose-on-amazon-linux-2/

https://gist.github.com/npearce/6f3c7826c7499587f00957fee62f8ee9#file-install-docker-md

https://floatingcloud.io/how-to-install-docker-and-compose-on-amazon-linux-2/

https://gist.github.com/npearce/6f3c7826c7499587f00957fee62f8ee9

https://www.adictosaltrabajo.com/2022/12/19/despliegue-de-aplicaciones-con-docker-compose/

https://computingforgeeks.com/install-and-use-docker-compose-on-fedora/


