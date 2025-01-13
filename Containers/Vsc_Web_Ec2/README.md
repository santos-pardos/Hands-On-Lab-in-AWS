## VSC in Ami Linux 2023

# Install
```
curl -Lk 'https://code.visualstudio.com/sha/download?build=stable&os=cli-alpine-x64' --output vscode_cli.tar.gz
tar -xf vscode_cli.tar.gz
```

# Launch
```
cd code
./code  tunnel --accept-server-license-terms --name vscode-demo-tunnel
```
Choose: Github Account
https://github.com/login/device 
2FA
enter code xxx-xxxx
https://vscode.dev/tunnel/vscode-demo-tunnel

# Automation
Connecting to the instance every time using Instance Connect to start the server is not that practical. Doing that from an Android tablet would work but I would rather try and automate that step a bit further.

What would be great is to be able to start VS Code server as a service that can run in the background. So first of all let us create a shell script, named vscodestart.sh, that will start the server.

#!/bin/sh
~/code  tunnel --accept-server-license-terms --name vscode-demo-tunnel
This is just the same command we used when we started it manually. Next we create a Linux service that we can start using systemd so let's create the service file named vscode.service.

[Unit]
After=network.target

[Service]
User=ec2-user
Group=ec2-user
ExecStart=/usr/local/bin/vscodestart.sh

[Install]
WantedBy=default.target
Now let's copy the vscode.service file to /etc/systemd/system/ and vscodestart.sh to /usr/local/bin/. We could now start the server using command:

sudo chmod 777 /etc/systemd/system/vscode.service
sudo chmod 777 /usr/local/bin/vscidestart.sh

sudo systemctl start vscode.service
sudo ssytemctl enable vscode.service


# Visual Studio Code - Docker and SSH Remote Extensions
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

# Link
```
https://jimmydqv.com/vscode-on-aws/
```