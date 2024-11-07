# Hands-On-Lab-in-AWS about containers and dockers

# Docker CE Install
```
sudo yum install docker -y
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

Reboot to verify it all loads fine on its own.
```
sudo reboot
```

# docker-compose install

Copy the appropriate docker-compose binary from GitHub:
```
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
```

Fix permissions after download:
```
sudo chmod +x /usr/local/bin/docker-compose
```

Verify success:
```
docker-compose version
```

# Visual studio Code - Docker extension - SSH Remote
permission denied while trying to connect to the Docker daemon socket at unix
https://www.baeldung.com/linux/docker-permission-denied-daemon-socket-error
```
ls -l /var/run/docker.sock
sudo chmod 666 /var/run/docker.sock
sudo systemctl restart docker.service

```


# Other Links
```
https://floatingcloud.io/how-to-install-docker-and-compose-on-amazon-linux-2/
https://gist.github.com/npearce/6f3c7826c7499587f00957fee62f8ee9#file-install-docker-md
```
