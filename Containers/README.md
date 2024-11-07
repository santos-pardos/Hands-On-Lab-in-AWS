# Hands-On-Lab-in-AWS about containers and dockers

 Install SSH remote extension 
 
 Install Docker exension

```
sudo dnf install docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
newgrp docker
```

Error VSC Docker extension in remote host: permission denied while trying to connect to the Docker daemon socket at unix

https://www.baeldung.com/linux/docker-permission-denied-daemon-socket-error
```
ls -l /var/run/docker.sock
sudo chmod 666 /var/run/docker.sock
sudo systemctl restart docker.service
```

# Docker CE Install
```
sudo dnf install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user
```
Make docker auto-start
```
sudo chkconfig docker on
```
Because you always need it....
```
sudo yum install -y git
```
Close the ssh session and enter again to execute docker with your user (ec2-user)
```
sudo systemctl status docker.service
```
# docker-compose install

## Option 1 (Linux AMI 2023)
```
sudo dnf -y install wget
sudo curl -s https://api.github.com/repos/docker/compose/releases/latest | grep browser_download_url | grep docker-compose-linux-x86_64 | cut -d '"' -f 4 | wget -qi -
sudo chmod +x docker-compose-linux-x86_64
sudo mv docker-compose-linux-x86_64 /usr/local/bin/docker-compose
docker-compose --version
```

## Option 2 (Linux AMI 2)
```
sudo yum install python3-pip
sudo pip3 install docker-compose
sudo systemctl enable docker.service
sudo systemctl start docker.service
```

## Option 3
Copy the appropriate docker-compose binary from GitHub:
```
sudo curl -L https://github.com/docker/compose/releases/download/1.3.1/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
```
Fix permissions after download:
```
sudo chmod +x /usr/local/bin/docker-compose
```
Verify success:
```
docker-compose version
```

# Other Links
```
https://www.cyberciti.biz/faq/how-to-install-docker-on-amazon-linux-2/
https://floatingcloud.io/how-to-install-docker-and-compose-on-amazon-linux-2/
https://gist.github.com/npearce/6f3c7826c7499587f00957fee62f8ee9#file-install-docker-md
https://floatingcloud.io/how-to-install-docker-and-compose-on-amazon-linux-2/
https://gist.github.com/npearce/6f3c7826c7499587f00957fee62f8ee9
https://www.adictosaltrabajo.com/2022/12/19/despliegue-de-aplicaciones-con-docker-compose/
https://computingforgeeks.com/install-and-use-docker-compose-on-fedora/
```

