
# Sistema de Turnos para Estética

Aplicación backend desarrollada en Python que permite gestionar turnos para un centro de estética.

El sistema permite registrar turnos, validar disponibilidad y visualizar los turnos existentes.

## Tecnologías utilizadas

* Python
* FastAPI
* SQLite
* Jinja2
* Uvicorn

## Funcionalidades

* Crear turnos para clientes
* Validar que no haya superposición de horarios
* Listar turnos registrados
* Gestión básica de servicios

## Estructura del proyecto

appturnos_fase1/

* main.py → rutas de la aplicación
* models.py → acceso a base de datos
* logic.py → lógica de negocio
* database.py → conexión a la base
* templates/ → vistas HTML

## Cómo ejecutar el proyecto

Clonar el repositorio:

git clone https://github.com/fernandojyaiy-art/sistema-turnos-estetica.git

Entrar en la carpeta del proyecto:

cd sistema-turnos-estetica

Instalar dependencias:

pip install fastapi uvicorn

Ejecutar el servidor:

uvicorn appturnos_fase1.main:app --reload

Abrir en el navegador:

http://127.0.0.1:8000

## Estado del proyecto

Fase 1 completada:

* creación de turnos
* validación de disponibilidad
* visualización de turnos


Escalabilidad futura

🚀 Próxima Fase – Fase 2

Motor de disponibilidad inteligente:

Control de camillas (2 en el mismo box)

Bloqueo automático de horarios

Validación de superposición

Tiempo obligatorio de desinfección

Cálculo automático según duración del servicio

🛠 Tecnologías

Python 3.13

SQLite

Arquitectura modular

Git

GitHub

🎯 Visión a Futuro

El sistema está diseñado para:

Adaptarse a múltiples estéticas

Convertirse en SaaS

Soportar múltiples sucursales

Implementar autenticación por local

Migrar a base de datos más robusta si fuera necesario

Proyecto en desarrollo activo.
Construido paso a paso con enfoque técnico, práctico y escalable.

Desarrollado por Matias Jyaiy como parte de su formación en backend profesional.