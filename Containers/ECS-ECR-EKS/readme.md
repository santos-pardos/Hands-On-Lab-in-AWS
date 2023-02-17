# Dockers and K8s examples

https://github.com/stacksimplify/kubernetes-fundamentals/tree/master/02-PODs-with-kubectl

https://www.stacksimplify.com/aws-eks/kubernetes-for-absolute-beginners/kubernetes-for-absolute-beginners/

AWS Doc

https://docs.aws.amazon.com/eks/latest/userguide/sample-deployment.html

kubectl get --all-namespaces pods

kubectl get pods

kubectl get deployments

kubectl run my-first-pod --image stacksimplify/kubenginx:1.0.0

kubectl expose pod my-first-pod  --type=NodePort --port=80 --name=my-first-service

kubectl expose pod my-first-pod  --type=NodePort --port=80 --target-port=80 --name=my-first-service3

kubectl port-forward my-first-pod 8080:80

kubectl get pods -o wide

kubectl get service

kubectl get svc

kubectl get nodes -o wide

kubectl describe pod my-first-pod 

kubectl logs my-first-pod

kubectl exec -it my-first-pod -- /bin/bash

  ls
  
  cd /usr/share/nginx/html
  
  cat index.html
  
  exit
  
  
kubectl exec -it my-first-pod ls


kubectl run nginx2 --image=nginx --requests=cpu=500m --expose --port=80

kubectl run YOUR_DEPLOYMENT_NAME --image=YOUR_IMAGE_URL --requests=cpu=500m --expose --port=YOUR_SERVICE_PORT

kubectl describe pods nginx2

kubectl exec -it nginx2 /bin/bash


kubectl create deployment nginx-deploy --image nginx

kubectl get deployments

kubectl get pods

kubectl describe deployment nginx-deploy

kubectl logs deployment/nginx-deploy

Buxybox (arrancar y parada)

kubectl run -i --tty busybox --image=busybox --restart=Never -- sh

kubectl run -i --rm --tty debug --image=busybox -- sh

kubectl run -i --tty utils --image=arunvelsriram/utils --restart=Never -- sh

sudo amazon-linux-extras install epel -y

sudo yum install stress -y


