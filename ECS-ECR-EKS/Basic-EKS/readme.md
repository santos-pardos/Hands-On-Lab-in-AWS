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

curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.16.8/2020-04-16/bin/linux/amd64/kubectl

chmod +x ./kubectl 

mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin 

kubectl version --short --client

# Install EKSCTL 

curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp

sudo mv /tmp/eksctl /usr/bin

eksctl version 

eksctl help

Connect AWS 

In AWS Academy - AWS Details - AWS CLI (copy all data in ~/.aws/credentials)

In AWS, the IAM user with EKS permisions 

aws configure 

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

eksctl create cluster --name dev-cluster --version 1.21 --region us-east-1 --nodegroup-name standard-workers --node-type t3.micro --nodes 3 --nodes-min 1 --nodes-max 4 --managed

In an AWS Academy (only in the zones a b c work the cluster)

eksctl create cluster --name dev-cluster --version 1.21 --region us-east-1 --zones us-east-1a,us-east-1b,us-east-1c --nodegroup-name standard-workers --node-type t3.micro --nodes 3 --nodes-min 1 --nodes-max 4 --managed


eksctl get cluster

aws eks update-kubeconfig --name dev-cluster --region us-east-1

sudo yum install -y git  

wget https://unir-profesantos.s3.eu-west-1.amazonaws.com/K8s-Basics-Deployments.zip 

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

kubectl get pod  

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

# Microservices Example
           
https://unir-profesantos.s3.eu-west-1.amazonaws.com/EKS-Microservices.zip
