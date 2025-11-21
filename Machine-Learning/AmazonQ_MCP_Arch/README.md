# Generación de Diagramas de Arquitectura AWS usando Amazon Q CLI + AWS Diagram MCP Server

Este documento describe los pasos necesarios para generar un diagrama de arquitectura AWS utilizando **Amazon Q CLI** y el **AWS Diagram MCP Server** en Amazon Linux 2023.

---

## 1. Instalar prerrequisitos en Amazon Linux 2023

### 1.0 Instalar Amazon Q
```bash
curl --proto '=https' --tlsv1.2 -sSf "https://desktop-release.q.us-east-1.amazonaws.com/latest/q-x86_64-linux.zip" -o "q.zip"
unzip q.zip
./q/install.sh
q login
q chat
```
### 1.1 Instalar GraphViz

GraphViz es necesario para que el MCP server pueda renderizar los diagramas.

```bash
sudo dnf install -y graphviz
```

### 1.2 Instalar `uv`

`uv` es el método recomendado para ejecutar el AWS Diagram MCP Server.

```bash
curl -Ls https://astral.sh/uv/install.sh | bash
source ~/.bashrc
uv --version
```

---

## 2. Configurar AWS Diagram MCP Server para Amazon Q CLI

Crear o editar el archivo de configuración para Amazon Q:

```bash
mkdir -p ~/.aws/amazonq
nano ~/.aws/amazonq/mcp.json
```

Colocar el siguiente contenido:

```json
{
  "mcpServers": {
    "awslabs.aws-diagram-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.aws-diagram-mcp-server"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "autoApprove": [],
      "disabled": false
    }
  }
}
```
```
{
  "mcpServers": {
    "awslabs.aws-diagram-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.aws-diagram-mcp-server"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "autoApprove": [],
      "disabled": false
    },
    "awslabs.aws-pricing-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.aws-pricing-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "autoApprove": [],
      "disabled": false
    }
  }
}

```
---

## 3. Verificar instalación de Amazon Q CLI

```bash
q --version
q login
```

Autenticarse con AWS Builder ID si es necesario.

---

## 4. Generar un diagrama de arquitectura con Amazon Q

Iniciar el chat interactivo:

```bash
q chat
```

Dentro del chat, usar un prompt como el siguiente:

```text
Using the AWS Diagram MCP server, generate an AWS architecture diagram for the following design and save it as a PNG in the current directory:

- One VPC with CIDR 10.0.0.0/16, DNS support enabled
- 2 Availability Zones
- 2 public subnets (one per AZ)
- 2 private subnets (one per AZ)
- 1 Bastion host (t3.micro) in a public subnet
- An Application Load Balancer in the public subnets
- 2 EC2 web servers (t3.micro) in the private subnets running Apache
- 1 database server (t3.small) in a private subnet running PostgreSQL
- NAT Gateways in the public subnets, used by the private subnets for outbound internet access
- Proper security groups: SSH only to bastion; HTTP/HTTPS from ALB to web servers; DB only accessible from web servers; no direct internet access to private instances.
Use official AWS icons and group resources by VPC and subnet.
```

Aprobar permisos cuando Amazon Q pregunte.

---

## 5. Localizar el diagrama generado

Listar archivos en el directorio actual:

```bash
ls
```

O buscar específicamente el PNG:

```bash
find . -maxdepth 2 -name "*.png"
```

---

## 6. Uso posterior del diagrama

Una vez generado:

- Puedes descargarlo vía `scp`
- Subirlo a S3. aws s3 cp fichero.png s3://mibucket/fichero.png
---

