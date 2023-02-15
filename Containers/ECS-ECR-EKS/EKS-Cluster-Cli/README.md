
# Command

eksctl create cluster -f cluster.yaml


eksctl delete cluster --region=us-east-1 --name=cluster-demo


aws eks --region xxxx create-cluster --name xxxxxx --role-arn xxxx --resources-vpc-config subnetIds=xxxx,xxxx,xxxx
