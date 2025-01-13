## VSC Web with Ami Linux 2023

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
```
Choose: Github Account
https://github.com/login/device 
2FA
enter code xxx-xxxx
https://vscode.dev/tunnel/vscode-demo-tunnel
```

# Automation
Create a vscodestart.sh file in /usr/local/bin/ directory:
```
sudo vim /usr/local/bin/vscodestart.sh
```
Add the code:
```
#!/bin/sh
~/code  tunnel --accept-server-license-terms --name vscode-demo-tunnel
```
Create a vscode.service file to /etc/systemd/system/ directory:
```
sudo vim/etc/systemd/system/vscode.service
```
```
[Unit]
After=network.target

[Service]
User=ec2-user
Group=ec2-user
ExecStart=/usr/local/bin/vscodestart.sh

[Install]
WantedBy=default.target
```

```
sudo chmod 777 /etc/systemd/system/vscode.service
sudo chmod 777 /usr/local/bin/vscodestart.sh

sudo systemctl start vscode.service
sudo systemctl enable vscode.service
```

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
