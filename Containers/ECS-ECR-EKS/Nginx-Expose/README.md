# Links

https://aws.amazon.com/es/premiumsupport/knowledge-center/eks-kubernetes-services-cluster/

kubectl apply -f nginx-deployment.yaml

kubectl get pods -l 'app=nginx' -o wide | awk {'print $1" " $3 " " $6'} | column -t


kubectl create -f clusterip.yaml

kubectl get service nginx-service-cluster-ip


kubectl create -f nodeport.yaml

kubectl get service/nginx-service-nodeport

kubectl get nodes -o wide |  awk {'print $1" " $2 " " $7'} | column -t

kubectl get nodes -o wide |  awk {'print $1" " $2 " " $6'} | column -t


kubectl create -f loadbalancer.yaml

kubectl get service/nginx-service-loadbalancer |  awk {'print $1" " $2 " " $4 " " $5'} | column -t

curl -silent *****.eu-west-1.elb.amazonaws.com:80 | grep title

kubectl delete service nginx-service-loadbalancer