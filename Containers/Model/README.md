# LLMs in Docker
```
docker model pull ai/llama3.2:1B-Q4_0
docker model run ai/llama3.2:1B-Q4_0
docker model run ai/llama3.2:1B-Q4_0 "Explica qué es Docker Model Runner"
```
## Docker Compose
```
services:
  model:
    image: ai/llama3.2:1B-Q4_0
    container_name: llama-1b
    runtime: nvidia
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
    ports:
      - "8080:8080"
    command: >
      --chat
```
```
curl http://localhost/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
        "model": "llama-1b",
        "messages": [{"role": "user", "content": "Hola, ¿qué puedes hacer?"}]
      }'

```


## LInks 
```
https://www.paradigmadigital.com/dev/ejecutando-llms-local-docker/
```
