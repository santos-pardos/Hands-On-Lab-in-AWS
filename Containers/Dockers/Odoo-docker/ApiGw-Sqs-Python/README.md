```
curl -X POST https://ci6oe0r1lb.execute-api.us-east-1.amazonaws.com/prod/pedido \
-H "Content-Type: application/json" \
-d '{"contacto": {"nombre": "Prueba"}, "producto": {"nombre": "Test", "precio_venta": 10}}'
```

```
curl -X POST https://ci6oe0r1lb.execute-api.us-east-1.amazonaws.com/prod/pedido \
-H "Content-Type: application/json" \
-d '{
  "contacto": {
    "nombre": "Prueba desde cURL",
    "email": "test-curl@sistemas.com"
  },
  "producto": {
    "nombre": "Monitor UltraWide",
    "precio_venta": 250.00,
    "coste": 190.00,
    "tipo": "consu",
    "referencia": "MON-UW-01",
    "codigo_barras": "123456789"
  }
}'
```


¿Qué tenemos ahora mismo configurado? 

    Action type: Use action name -> SendMessage

    HTTP Headers: Content-Type -> 'application/x-www-form-urlencoded'

    Mapping Template (application/json): Action=SendMessage&QueueUrl=https://sqs.us-east-1.amazonaws.com/658620698452/odoo&MessageBody=$util.urlEncode($input.body)




AWS Region

us-east-1
AWS service

Simple Queue Service (SQS)
AWS subdomain
HTTP method

POST
Action type
Use action name
Use path override
Action name
SendMessage
Execution role
arn:aws:iam::658620698452:role/LabRole
Credential cache

Do not add caller credentials to cache key
Content handling
Learn more 

Passthrough
Integration timeout
Info
By default, you can enter an integration timeout of 50 - 29,000 milliseconds. You can use Service Quotas to raise the integration timeout to greater than 29,000 ms
29000
Request body passthrough
When there are no templates defined (recommended)
When no template matches the request content-type header
Never
If you set the request body passthrough to When no templates matches the request content-type header, API Gateway will pass all request payloads directly to the endpoint without transformation, and will transform any matches for the incoming content type. To secure your integration, select When there are no templates defined (recommended).
URL path parameters
URL query string parameters
URL request headers parameters
Name
Content-Type
Mapped from Info
'application/x-www-form-urlencoded'
Caching
Remove
Add request header parameter
Mapping templates
Content type
application/json
Generate template

Template body
Action=SendMessage&QueueUrl=https://sqs.us-east-1.amazonaws.com/658620698452/odoo&MessageBody=$util.urlEncode($input.body)
