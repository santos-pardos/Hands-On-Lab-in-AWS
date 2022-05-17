# TOOLS (Linux)
(look on The Internet for the Windows and MAC tools)

aws --version

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

unzip awscliv2.zip

which aws \
./aws/install --bin-dir /usr/bin --install-dir /usr/bin/aws-cli --update \
aws --version

aws configure

curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.16.8/2020-04-16/bin/linux/amd64/kubectl

chmod +x ./kubectl \
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin \
kubectl version --short --client

curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp

sudo mv /tmp/eksctl /usr/bin

eksctl version \
eksctl help


----------------------------------------------------
# K8S CLUSTER on EKS

eksctl create cluster --name dev-cluster --version 1.21 --region us-east-1 --nodegroup-name standard-workers --node-type t3.micro --nodes 3 --nodes-min 1 --nodes-max 4 --managed

eksctl get cluster

aws eks update-kubeconfig --name dev-cluster --region us-east-1

sudo yum install -y git  \
git clone https://github.com/ACloudGuru-Resources/Course_EKS-Basics  \
ls  \
cd Course_EKS-Basics/  \
cat nginx-deployment.yaml  \
cat nginx-svc.yaml  

kubectl apply -f ./nginx-svc.yaml  

kubectl get service  \
           "a06d451f9de2b4dceb100a6fflcb15c2-1122912181.us-east-1.elb.amazonaws.com"  

kubectl apply -f ./nginx-deployment.yaml  \
kubectl get deployment  \
kubectl get pods  \
kubectl get rs  \
kubectl get node \ 
kubectl get service \
kubectl get replicaset


curl "a06d451f9de2b4dceb100a6fflcb15c2-1122912181.us-east-1.elb.amazonaws.com"  


kubectl get node  \
kubectl get namespaces \
kubectl get pod  \
kubectl exec -it tetris-86cd7c55c7-8mwtd -- /bin/bash   

kubectl delete pod two-containers 

kubectl delete deployment two-containers

eksctl delete cluster dev-cluster
