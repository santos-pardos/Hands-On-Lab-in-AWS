## Links

https://kubernetes.io/es/docs/concepts/workloads/controllers/jobs-run-to-completion/

https://howtoforge.es/trabajos-en-kubernetes/


## Commands

kubectl apply -f https://k8s.io/examples/controllers/job.yaml

kubectl describe jobs/pi

pods=$(kubectl get pods --selector=job-name=pi --output=jsonpath='{.items[*].metadata.name}')

echo $pods

kubectl logs $pods
