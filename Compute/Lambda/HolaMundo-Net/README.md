## Instalar .NET SDK 8 en Amazon Linux 2023

1.1 Actualiza e instala utilidades básicas
```
sudo dnf update -y
sudo dnf install -y curl unzip zip tar gzip
```

1.2 Añade el repo de Microsoft para amazonlinux/2023
```
curl -sSL -O https://packages.microsoft.com/config/amazonlinux/2023/packages-microsoft-prod.rpm
sudo rpm -i packages-microsoft-prod.rpm
rm -f packages-microsoft-prod.rpm
sudo dnf update -y
```

Esto sigue el flujo recomendado para repos RPM de Microsoft.

1.3 Instala el SDK 8
```
sudo dnf install -y dotnet-sdk-8.0
```

1.4 Verifica
```
dotnet --version
dotnet --list-sdks
```

## Instalar Amazon.Lambda.Tools (CLI “dotnet lambda …”)
2.1 Instala la herramienta global
```
dotnet tool install -g Amazon.Lambda.Tools
```

(Esto es lo que indica NuGet para el tool global).

2.2 Asegura que ~/.dotnet/tools está en el PATH

En AL2023 muchas veces no queda en PATH por defecto. Añádelo:

Bash (ec2-user)
```
echo 'export PATH="$PATH:$HOME/.dotnet/tools"' >> ~/.bashrc
source ~/.bashrc
```

(En zsh sería ~/.zshrc.)

2.3 Comprueba que funciona

```
dotnet lambda --help
```

AWS documenta ese comando para listar/usar las órdenes de Lambda