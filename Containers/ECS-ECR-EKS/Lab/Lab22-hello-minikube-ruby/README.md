# Helloworld Ruby Application in Kubernetes (minikube)

## Overview
This repository contains a sample "hello world" application written in Ruby. The repository contains also the required files to build the application as a Docker container and deploy it in a Kubernetes cluster as a load balanced service.

The application is presented as a simple web service that returns a web page with the following message:

```
Hello world! my IP is <pod ip>
```

where `pod ip` is the IP given to the backend pod. This way we can verify that the application is load balanced correctly. In this scenario the application is load balanced between 2 pods.

## Description of files

`helloworld.rb` : The sample Ruby application. This can be ran as a standalone app (e.g. for testing purposes) by using `ruby helloworld.rb`. The application runs a simple web server on port `8080` and returns a simple page as described before.

`helloworld.dockerfile` : This is the Docker configuration that can be used to build the container image for the application. The configuration exposes port 8080 from the container to the host running the container.

`helloworld-deployment.yaml` : This is the YAML configuration required to create a Kubernetes deployment using the container image created for the sample application. The deployment defines a replica set of 2 pods and port 8080 as the one to be used to access the application on the running container.

`helloworld-service.yaml` : This is the YAML configuration required to create a Kubernetes service to load balance requests to the application between all the pods and to expose the service onto the IP of the cluster node on a pre-defined port (port `31000` in the sample configuration)

## Assumptions

* Using a Linux/Mac system as the host for running the `minikube` cluster.

## Prerequisites

* Install `minikube` following the instructions from https://kubernetes.io/docs/tasks/tools/install-minikube/ depending on your operating system.

## Deploying the application

The application was provided as a zip file so after unzipping you should have a folder called `hello-minikube-ruby`. Open a terminal and `cd` into that folder to facilitate running the required commands.

### Verify your minikube installation

From the terminal run:

```
kubectl cluster-info
```

You should get an output similar to

```
Kubernetes master is running at https://192.168.99.100:8443
KubeDNS is running at https://192.168.99.100:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
```

From the terminal run:

```
kubectl get nodes
```

You should get an output similar to:

```
NAME       STATUS    ROLES     AGE       VERSION
minikube   Ready     master    3d        v1.13.4
```

### Create the container image
The first step to deploy the application is to create the container image that we will use to run the application in the cluster.

In order to do that we first need to run the command to use the Docker environment from the `minikube` cluster. From the terminal run:

```
eval $(minikube docker-env)
```

Then from the same terminal we run the following commands to build the container image:
```
docker build -t helloworld:0.0.1 -f helloworld.dockerfile .
```

Then verify that the image was created:
```
docker images
```

You should see the image in the output similar to:

```
REPOSITORY                                TAG                 IMAGE ID            CREATED             SIZE
helloworld                                0.0.1               34052bc5ef21        37 minutes ago      873MB
```

### Create the deployment
In order to create the deployment of the application in the Kubernetes cluster you need to run the following command from the terminal:

```
kubectl create -f helloworld-deployment.yaml
```

This command should return with an output similar to:

```
deployment.apps "helloworld" created
```

Then verify that the deployment was created by running:

```
kubectl get deployments
```

You should get an output similar to:

```
NAME         DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
helloworld   2         2         2            2           39m
```

Note the `DESIRED` and `CURRENT` count which denote the number of pods that we want to use and how many to we currently have.

### Create the service

In order to create the service to load balance the application in the Kubernetes cluster you need to run the following command from the terminal:

```
kubectl create -f helloworld-service.yaml
```

This command should return with an output similar to:

```
service "helloworld" created
```

Then verify that the service was created by running:

```
kubectl get services
```

You should get an output similar to:

```
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
helloworld   LoadBalancer   10.111.20.145   <pending>     80:31000/TCP   41m
kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP        3d
```

The `CLUSTER-IP` in your case might be different but the ports should indicate the port that the cluster is using to access the application (80) and the port that the cluster node exposes to the world to access the application (31000)

### Test

Run the `kubectl cluster-info` command again to get the IP of the cluster node:

```
Kubernetes master is running at https://192.168.99.100:8443
KubeDNS is running at https://192.168.99.100:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
```

From a browser use that IP and port 31000 to access the application. From the terminal we can use the `curl` command:

```
curl http://192.168.99.100:31000
```

You should get an output similar to the following:

```
Hello world! my IP is 172.17.0.6
```

Run the command multiple times and you will see that the IP changes to reflect that the requests are load balanced between the pods.

## Remove the application

To tear down the service and deployment run the following commands:

```
kubectl delete service helloworld
```
```
kubectl delete deployment helloworld
```

To delete the container image run:

```
docker image rm $(docker images --filter reference=helloworld* --format "{{.ID}}")
```
