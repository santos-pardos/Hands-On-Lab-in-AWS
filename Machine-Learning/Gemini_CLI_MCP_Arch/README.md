# Generación de Diagramas de Arquitectura AWS usando Gemini CLI + AWS Diagram MCP Server

Este documento describe los pasos necesarios para generar un diagrama de arquitectura AWS utilizando **eEmini CLI** y el **AWS Diagram MCP Server** en Ubuntu 24

---

## 1. Instalar prerrequisitos en Amazon Linux 2023

### 1.0 Instalar Gemini Cli
```bash
sudo apt-get update
sudo apt-get install nodejs -y
sudo apt-get install npm -y
curl -fsSL https://deb.nodesource.com/setup_23.x -o nodesource_setup.sh
sudo -E bash nodesource_setup.sh
sudo apt-get install nodejs -y
sudo apt-get install npm -y
sudo npm install -g @google/gemini-cli
gemini
```
### 1.1 Instalar uv y GraphViz

GraphViz es necesario para que el MCP server pueda renderizar los diagramas.

```bash
pipx install uv  # o según tu SO
uv python install 3.10
sudo apt-get install graphviz
```

### 1.2 Añadir MCP Server con gemini mcp add

```bash
gemini mcp add \
  -s user \
  -e FASTMCP_LOG_LEVEL=ERROR \
  awslabs.aws-diagram-mcp-server \
  uvx awslabs.aws-diagram-mcp-server
```
```
cat .gemini/settings.json
gemini mcp list
```

### 1.3 Configurar AWS Diagram MCP Server para Amazon Q CLI

Crear o editar el archivo de configuración para Amazon Q:

```bash
mkdir -p ~/.aws/amazonq
nano ~/.aws/amazonq/mcp.json
```




