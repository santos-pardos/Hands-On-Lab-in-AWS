# create namespace
to separate your cluster resources logically it is *best practice* to use _namespaces_. You can separate either by project, customer, team, environment,...
The benefit you gain is by getting control over resource qoutas, access control etc

```
kubectl create namespace ns-eks-course
```
