# Dockerfile para la aplicación de calculadora Flask

# Imagen base de Python 3.13
FROM python:3.13-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivo de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código de la aplicación
COPY . .

# Exponer el puerto 3000
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]