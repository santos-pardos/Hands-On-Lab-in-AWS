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

# Visual studio Code - Docker - SSH Remote
```
Read more about SSH config files: https://linux.die.net/man/5/ssh_config
Host 3.249.102.215
    HostName 3.249.102.215
    User ec2-user
    IdentityFile c:\000\VSCode.pem
```

permission denied while trying to connect to the Docker daemon socket at unix

https://www.baeldung.com/linux/docker-permission-denied-daemon-socket-error
```
ls -l /var/run/docker.sock
sudo chmod 666 /var/run/docker.sock
sudo systemctl restart docker.service

```

# Visual studio Code - Docker - SSH Remote
```
# This will start a code-server container and expose it at http://127.0.0.1:8080.
# It will also mount your current directory into the container as `/home/coder/project`
# and forward your UID/GID so that all file system operations occur as your user outside
# the container.
#
# Your $HOME/.config is mounted at $HOME/.config within the container to ensure you can
# easily access/modify your code-server config in $HOME/.config/code-server/config.json
# outside the container.
```
```
mkdir -p ~/.config
docker run -it --name code-server2 -p 8080:8080 \
  -v "$HOME/.local:/home/coder/.local" \
  -v "$HOME/.config:/home/coder/.config" \
  -v "$PWD:/home/coder/project" \
  -u "$(id -u):$(id -g)" \
  -e "DOCKER_USER=$USER" \
  codercom/code-server:latest
```

# Other Links
```
https://floatingcloud.io/how-to-install-docker-and-compose-on-amazon-linux-2/
https://gist.github.com/npearce/6f3c7826c7499587f00957fee62f8ee9#file-install-docker-md
```
