## Links
https://rajanieshkaushikk.com/2021/02/27/how-to-deploy-sql-server-containers-to-a-kubernetes-cluster-for-high-availability/


## EKS Secret
kubectl create secret generic mssql-secret --from-literal=SA_PASSWORD="example_123"


## Secrets
echo -n "example_123" | base64                                                                                                                           
ZXhhbXBsZV8xMjM=
