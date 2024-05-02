# USJ Workshop Architecture

![](CF-WAF-ALB-EC2.png)

## EC2
```
#!/bin/bash 
dnf update -y 
dnf install -y docker 
service docker start 
systemctl enable docker.service
docker pull santospardos/usj:juiceshop
docker run -d -p 80:3000 santospardos/usj:juiceshop
```

## ELB
```
TG
ALB
```
## CloudFront - WAF 
```
Distribution with ALB like origin.
```
## SQL Inyection and Cross-site scripting attacks
```
export JUICESHOP_URL=xxxxxxxALB-DNSxxxxxxxx
curl -X POST  $JUICESHOP_URL -F "user='<script><alert>Hello></alert></script>'"
curl -X POST $JUICESHOP_URL -F "user='AND 1=1;"
```


