

## Install CSI EFS Drivers

kubectl apply -k "github.com/kubernetes-sigs/aws-efs-csi-driver/deploy/kubernetes/overlays/stable/?ref=release-1.3"

kubectl get pods -n kube-system

## Info CSI EFS Drivers

https://github.com/kubernetes-sigs/aws-efs-csi-driver/tree/master



##Example

https://github.com/kubernetes-sigs/aws-efs-csi-driver/tree/master/examples/kubernetes/statefulset
