# LLMs in Docker
```
docker model pull ai/llama3.2:1B-Q4_0
docker model run ai/llama3.2:1B-Q4_0
docker model run ai/llama3.2:1B-Q4_0 "Explica qué es Docker Model Runner"
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


## LInks 
```
https://www.paradigmadigital.com/dev/ejecutando-llms-local-docker/
```
