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
