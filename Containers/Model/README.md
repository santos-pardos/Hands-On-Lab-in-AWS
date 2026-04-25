# LLMs in Docker
## Insgtall Docker in Ubuntu
```
sudo apt update && sudo apt upgrade -y
```
```
# Add Docker's official GPG key:
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update
```
```
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo usermod -aG docker $USER
newgrp docker
```
```
sudo apt-get install docker-model-plugin
docker model version
```
```
docker model pull ai/llama3.2:1B-Q4_0
docker model run ai/llama3.2:1B-Q4_0
docker model run ai/llama3.2:1B-Q4_0 "Explica qué es Docker Model Runner"
docker ps
docker model list
docker model status
docker model unload ai/llama3.2:1B-Q4_0

```
```
curl -s http://localhost:12434/engines/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.2:1B-Q4_0",
    "messages": [
      {"role": "user", "content": "hola"}
    ]
  }' | jq -r '.choices[0].message.content'
```
## Steps
```
docker model ps
```
# Precalentamiento
```
docker model run llama3.2:1B-Q4_0 "hola"
```
```
curl -s http://localhost:12434/engines/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.2:1B-Q4_0",
    "messages": [
      {"role": "user", "content": "ping"}
    ],
    "max_tokens": 1
  }'
```
```
docker model ps
```

## Gemma
```
docker model search gemma
```
```
docker model pull ai/gemma3
```
```
docker model run ai/gemma3
```
```
curl http://localhost:12434/engines/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "ai/gemma:2b",
    "messages": [
      {"role": "user", "content": "hola"}
    ]
  }'
```

## LInks 
```
https://www.paradigmadigital.com/dev/ejecutando-llms-local-docker/
```
