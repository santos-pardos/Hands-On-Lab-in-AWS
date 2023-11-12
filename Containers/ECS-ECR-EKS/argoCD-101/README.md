## EKS - ArgoCD

```
eksctl get cluster
aws eks update-kubeconfig --name demo-cluster --region us-east-1

kubectl create namespace argocd 
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.4.7/manifests/install.yaml
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'
export ARGOCD_SERVER=`kubectl get svc argocd-server -n argocd -o json | jq --raw-output '.status.loadBalancer.ingress[0].hostname'`
echo $ARGOCD_SERVER
export ARGO_PWD=`kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d`
echo $ARGO_PWD

Repositories : git - default  - https://github.com/santos-pardos/Tetris-Game.git and Connect
New App; tetris - default - Automatic - https://github.com/santos-pardos/Tetris-Game.git - manifests  - https://Kubernetes.default.svc - default - Create

kubectl get all
kubectl delete svc argocd-server -n argocd
```


## Repositorio

```
https://github.com/santos-pardos/Tetris-Game.git
```

##  Links

```
https://aws.plainenglish.io/gitops-deploying-tetris-on-eks-using-argocd-3836569fb4c1
https://medium.com/@surendar.grind/gitops-a-begineer-guide-2ca1fded446e
```
