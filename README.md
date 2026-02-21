
🧴 Sistema de Turnos – Clínica Estética

Backend desarrollado en Python + SQLite para la gestión de turnos en una clínica estética real.

Este proyecto está construido de manera modular y escalable, siguiendo una evolución por fases, priorizando aprendizaje profundo y arquitectura sólida antes de pensar en SaaS.

📌 Estado del Proyecto
✅ Fase 0 – MVP Funcional

Creación básica de turnos

Persistencia en SQLite

Estructura inicial modular

Proyecto subido a GitHub

Separación básica por archivos

Objetivo: validar que el sistema funcione de punta a punta.

✅ Fase 1 – Modelado Profesional de Base de Datos

Rediseño completo del modelo relacional.

Mejoras implementadas:

Separación clara por capas:

database.py → conexión a la base

models.py → acceso a datos

logic.py → reglas de negocio

main.py → punto de entrada

Creación de tablas:

clientes

servicios

turnos

turno_clientes (tabla intermedia)

Soporte para:

Turnos individuales

Turnos promocionales (2 clientes)

Historial independiente por cliente

Duración variable por servicio

🧠 Arquitectura del Sistema
Usuario
   ↓
main.py
   ↓
logic.py
   ↓
models.py
   ↓
database.py
   ↓
SQLite

Cada capa tiene una responsabilidad específica:

main → Orquestación

logic → Reglas del negocio

models → Operaciones SQL

database → Infraestructura

Esto evita código mezclado y permite escalar sin romper todo.

🗄 Modelo Relacional
clientes

Información individual de cada persona.

servicios

Duración y características del tratamiento.

turnos

Fecha, hora, estado.

turno_clientes

Relaciona uno o dos clientes con un turno.

Esto permite:

Promociones de 2 personas

Privacidad controlada (mismo box)

Historial clínico individual

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

Desarrolado por Matias Jyaiy.