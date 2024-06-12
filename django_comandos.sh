#!/bin/bash

# Cambia al directorio de tu proyecto Django
cd /usr/src/app

# Copia el archivo requirements.txt al directorio actual
COPY requirements.txt ./

# Instala los requisitos del proyecto
RUN pip install -r requirements.txt

# Copia todos los archivos al directorio actual
COPY . .

# Ejecuta las migraciones de la base de datos
python manage.py makemigrations
python manage.py migrate
