# LLMs in Docker
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

## LInks 
```
https://www.paradigmadigital.com/dev/ejecutando-llms-local-docker/
```
