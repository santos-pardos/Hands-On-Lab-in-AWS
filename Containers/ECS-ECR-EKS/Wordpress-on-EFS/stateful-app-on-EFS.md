 # create namespace
```
kubectl create namespace ns-eks-course-efs
```

# create storage
The steps to execute are:  

1. add RBAC to access EFS
2. create EFS provisioner  
replace your *EFS-ID* and *EFS-DNS name* in file _create-efs-provisioner.yaml_
3. create PVCs

The corresponding commands are:  
```
kubectl apply -f create-rbac.yaml --namespace=ns-eks-course-efs
helm repo add aws-efs-csi-driver  https://kubernetes-sigs.github.io/aws-efs-csi-driver/
kubectl get pod -n default -l app.kubernetes.io/name=aws-efs-csi-driver,app.kubernetes.io/instance=aws-efs-csi-driver
kubectl apply -f create-storage.yaml --namespace=ns-eks-course-efs
```

# deploy mysql
## create secret which stores mysql pw, to be injected as env var into container
```
kubectl create secret generic mysql-pass --from-literal=password=eks-course-mysql-pw --namespace=ns-eks-course-efs
```
check:
```
kubectl get secrets --namespace=ns-eks-course-efs
```

## launch mysql deployment
```
kubectl apply -f deploy-mysql.yaml --namespace=ns-eks-course-efs
```
## checks
* persistent volumes
* persistent volume claims
* pods
```
kubectl get pv --namespace=ns-eks-course-efs
kubectl get pvc --namespace=ns-eks-course-efs
kubectl get pods -o wide --namespace=ns-eks-course-efs
```

# deploy wordpress
```
kubectl apply -f deploy-wordpress.yaml --namespace=ns-eks-course-efs
```
get URL of the app:
```
kubectl describe service wordpress --namespace=ns-eks-course-efs | grep Ingress
```
or goto AWS console => EC2

```

