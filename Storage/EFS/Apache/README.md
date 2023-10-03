## One Apache with EFS System

## Install Linux and Apache

```
sudo dnf install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
```

curl localhost
http://public ip/

## EFS system


cd /var/www/html
mkdir efs
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-0f2512d76577aa529.efs.us-east-1.amazonaws.com:/ efs
(you can read this command in Attach options in EFS service into AWS)
df -h

