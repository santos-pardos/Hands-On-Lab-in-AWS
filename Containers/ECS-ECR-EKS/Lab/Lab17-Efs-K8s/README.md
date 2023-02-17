# Links

NOTE: Open SGEFS the 2049 port

kubectl apply -k "github.com/kubernetes-sigs/aws-efs-csi-driver/deploy/kubernetes/overlays/stable/?ref=release-1.3"

kubectl get pods -n kube-system

kubectl apply -f efs-pvc.yaml

kubectl get pvc -n storage

kubectl get pv

kubectl apply -f efs-writer.yaml

kubectl apply -f efs-reader.yaml



