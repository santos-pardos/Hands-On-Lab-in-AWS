
# Command

eksctl create cluster -f cluster.yaml


eksctl delete cluster --region=us-east-1 --name=cluster-demo


aws eks --region <region> create-cluster --name <clusterName> --role-arn <EKS-role-ARN> --resources-vpc-config subnetIds=<subnet-id-1>,<subnet-id-2>,<subnet-id-3>
