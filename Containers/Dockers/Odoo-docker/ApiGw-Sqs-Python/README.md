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
