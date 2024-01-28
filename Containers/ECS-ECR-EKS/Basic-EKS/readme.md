# Install Eksctl & Kubectl TOOLS (Linux)
(windows and MAC on the Internet)


AWS Tools (in Cloud9 you dont need to install AWS Tools) \
aws --version

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

unzip awscliv2.zip

which aws \
./aws/install --bin-dir /usr/bin --install-dir /usr/bin/aws-cli --update \
aws --version

# Install KUBECTL 

curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.28.3/2023-11-14/bin/linux/amd64/kubectl

chmod +x ./kubectl 

mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin 

kubectl version --client

# Install EKSCTL 

ARCH=amd64

(for ARM systems, set ARCH to: `arm64`, `armv6` or `armv7`)

PLATFORM=$(uname -s)_$ARCH

curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$PLATFORM.tar.gz"

tar -xzf eksctl_$PLATFORM.tar.gz -C /tmp && rm eksctl_$PLATFORM.tar.gz

sudo mv /tmp/eksctl /usr/local/bin

eksctl version 

eksctl help

Connect AWS 

In AWS Academy - AWS Details - AWS CLI (copy all data in ~/.aws/credentials)

In AWS, the IAM user with EKS permisions 

aws configure 

# Install HELM

curl -sSL https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

helm version --short

2 option

Download your desired version  https://github.com/helm/helm/releases

Unpack it (tar -zxvf helm-v3.0.0-linux-amd64.tar.gz)

Find the helm binary in the unpacked directory, and move it to its desired destination (mv linux-amd64/helm /usr/local/bin/helm)

# Install HELM (just in case)
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 > get_helm.sh

chmod 700 get_helm.sh

./get_helm.sh

helm version --short | cut -d + -f 1

# Upload docker to ECR

(I have a docker, builted or downloaded)
docker run -dp 80:80 2048

aws configure

aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin xxxxxxxx.dkr.ecr.eu-west-1.amazonaws.com

docker tag jupyter/minimal-notebook:latest xxxxxxxx.dkr.ecr.eu-west-1.amazonaws.com/demo-sv:2048

docker push xxxxxx.dkr.ecr.eu-west-1.amazonaws.com/demo-sv:2048



----------------------------------------------------
# K8S CLUSTER on EKS

In an AWS Account

eksctl create cluster --name demo-cluster --version 1.26 --region us-east-1 --nodegroup-name standard-workers --node-type t3.micro --nodes 3 --nodes-min 1 --nodes-max 4 --managed

eksctl create cluster -f Cluster.yaml

In an AWS Academy (only in the zones a b c work the cluster)

eksctl create cluster --name demo-cluster --version 1.26 --region us-east-1 --zones us-east-1a,us-east-1b,us-east-1c --nodegroup-name standard-workers --node-type t3.micro --nodes 3 --nodes-min 1 --nodes-max 4 --managed


eksctl get cluster

aws eks update-kubeconfig --name demo-cluster --region us-east-1

sudo yum install -y git  

wget https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/code/EKS-SVCs-Deployments.zip

(wget https://unir-profesantos.s3.eu-west-1.amazonaws.com/K8s-Basics-Deployments.zip)

cd Course_EKS-Basics/  

cat nginx-deployment.yaml  

cat nginx-svc.yaml  

kubectl apply -f ./nginx-svc.yaml  

kubectl get service  
           "xxxxxxxxx.us-east-1.elb.amazonaws.com"         
           
curl "a06d451f9de2b4dceb100a6fflcb15c2-1122912181.us-east-1.elb.amazonaws.com"  

kubectl apply -f ./nginx-deployment.yaml  

kubectl get deployment  

kubectl get pods  

kubectl get rs  

kubectl get node 

kubectl get service 

kubectl get replicaset 

kubectl get node  

kubectl get namespaces 

kubectl get all --all-namespaces

kubectl get pod  

kubectl -n kube-system get all

kubectl -n kube-system get pods

 kubectl run nginx --image=nginx

kubectl port-forward my-service 8000:80

kubectl exec -it tetris-86cd7c55c7-8mwtd -- /bin/bash   

kubectl exec -ti worker-hello-5bfdf775d7-46f2g sh

aws eks list-clusters 

aws eks describe-cluster --name <insertclustername> 

kubectl cluster-info
           
kubectl scale deployment ecsdemo-nodejs --replicas=3 

kubectl scale deployment ecsdemo-crystal --replicas=3

kubectl apply -f kubernetes/deployment.yaml 

kubectl apply -f kubernetes/service.yaml

kubectl config set-context --current --namespace=default
           
kubectl get pods --all-namespaces

kubectl delete pod two-containers 

kubectl delete deployment two-containers

eksctl delete cluster dev-cluster

Logs

kubectl describe pod xxxxxxx

docker inspect santospardos/sanvalero:azuresql

kubectl logs -f deploy/mssql-sample-deployment

kubectl exec -it pod/mssql-deployment-7f55b56bc9-l5gn9 /bin/bash

# Links

https://www.bluematador.com/learn/kubectl-cheatsheet

# Microservices Example
           
https://unir-profesantos.s3.eu-west-1.amazonaws.com/EKS-Microservices.zip

# Error loggin server

Edit the file: $ cat ~/.aws/credentials

Remove the token and the region lines (left only these)

[default]

aws_access_key_id = AKIA2HW7LBNS5

aws_secret_access_key = 9phAAEUyPr1mmlZTqjiWBpu5ynkp3b
