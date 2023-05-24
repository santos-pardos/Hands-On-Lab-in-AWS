eksctl get cluster

aws eks update-kubeconfig --name demo --region us-east-1
kubectl config current-context

kubectl config view

kubectl get all -A

kubectl get pods --all-namespaces

kubectl get pods -n kube-system

kubectl get all --namespace kube-system

kubectl create namespace test

kubectl get namespace

kubectl delete ns test

```
kind: Namespace
apiVersion: v1
metadata:
  name: test
  labels:
    name: test
```

kubectl apply -f test.yaml

```
apiVersion: v1
kind: Pod
metadata:
  name: mypod
  labels:
    name: mypod
spec:
  containers:
  - name: mypod
    image: nginx
```

kubectl apply -f pod.yaml --namespace=test

```
apiVersion: v1
kind: Pod
metadata:
  name: mypod
  namespace: test
  labels:
    name: mypod
spec:
  containers:
  - name: mypod
    image: nginx

```

$ kubectl get pods

No resources found.

$ kubectl get pods --namespace=test

NAME      READY     STATUS    RESTARTS   AGE

mypod     1/1       Running   0          10s

 kubectl exec -it  mypod --namespace=test bash  
 
root@mypod:/usr/share/nginx# ls



kubectl run nginx-dev --image=nginx

kubectl delete deployment nginx-dev

kubectl create -f pod.yaml

kubectl delete pod mypod

kubectl apply -f netshoot.yaml 


kubectl create ns express-nodejs

kubectl apply -f https://raw.githubusercontent.com/LukeMwila/setting-up-eks-cluster-dojo/master/manifests/pod.yaml

kubectl get pods -o wide --namespace=express-nodejs

kubectl port-forward express-test 8080:8080 --namespace=express-nodejs

http://localhost:8080/test

kubectl run -it utils --image=arunvelsriram/utils -- sh

kubectl run -it utils2 --image=arunvelsriram/utils  -- sh

Ifconfig y ping de una a otra


kubectl run my-first-pod --image stacksimplify/kubenginx:1.0.0

kubectl expose pod my-first-pod --type=NodePort --port=80 --target-port=80 --name=my-first-service3

kubectl get pods -o wide

kubectl get all -o wide

http:ipdondeestaelnodo:puertoefimero
