## Deployment

First, create the volume that Portainer Server will use to store its database:

```
docker volume create portainer_data
```
```
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
```

By default, Portainer generates and uses a self-signed SSL certificate to secure port 9443. Alternatively you can provide your own SSL certificate during installation or via the Portainer UI after installation is complete.

If you require HTTP port 9000 open for legacy reasons, add the following to your docker run command:

-p 9000:9000

Portainer Server has now been installed. You can check to see whether the Portainer Server container has started by running docker ps:


## Links
```
https://docs.portainer.io/start/install-ce/server/docker/linux
```
