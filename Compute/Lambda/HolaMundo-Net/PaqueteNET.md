## Camino rápido sin Visual Studio 

Suponiendo que tienes .NET SDK 8 y Amazon.Lambda.Tools instalado (como hiciste en AL2023):

1) Crear proyecto Lambda

```
dotnet new -i Amazon.Lambda.Templates
dotnet new lambda.EmptyFunction -n HolaMundo
cd HolaMundo
```

2) Pega el Function.cs

Reemplaza src/HolaMundo/Function.cs con el código “Hola mundo” que te pasé.

3) Empaquetar ZIP

Desde la carpeta del proyecto:
```
dotnet lambda package -c Release -o function.zip
```
4) Subirlo a Lambda

Consola AWS: Lambda → Code → Upload from → .zip file → function.zip
o CLI:

aws lambda update-function-code \
  --function-name NOMBRE_DE_TU_LAMBDA \
  --zip-file fileb://function.zip

5) Handler

En Lambda → Runtime settings → Handler:
```
HolaMundo::HolaMundo.Function::FunctionHandler
```