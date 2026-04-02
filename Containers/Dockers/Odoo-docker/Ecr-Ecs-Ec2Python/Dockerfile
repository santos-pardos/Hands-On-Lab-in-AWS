# Usamos Debian 12 (Bookworm), moderno, estable y con soporte activo
FROM python:3.10-bookworm

# Actualizamos repositorios e instalamos wkhtmltopdf
RUN apt-get update && apt-get install -y wkhtmltopdf

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos los requisitos y los instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código de la API
COPY app.py .

# Exponemos el puerto 5000
EXPOSE 5000

# Arrancamos la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
