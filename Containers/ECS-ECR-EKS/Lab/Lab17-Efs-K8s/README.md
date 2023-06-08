# Links

https://archive.eksworkshop.com/beginner/190_efs/efs-csi-driver/

NOTE: Open SGEFS the 2049 port

### Install CSI EFS Drivers

kubectl apply -k "github.com/kubernetes-sigs/aws-efs-csi-driver/deploy/kubernetes/overlays/stable/?ref=release-1.3"



kubectl get pods -n kube-system

kubectl apply -f efs-pvc.yaml

kubectl get pvc 

kubectl get pv

kubectl apply -f efs-writer.yaml

kubectl exec -it efs-writer -- tail /shared/out.txt

kubectl apply -f efs-reader.yaml



