# ========================
# IMPORTS
# ========================

from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from appturnos.database import create_table, get_connection


# ========================
# APP
# ========================

app = FastAPI()

templates = Jinja2Templates(directory="appturnos/templates")

# Crear tabla al iniciar
create_table()

# ========================
# RUTAS
# ========================

@app.get("/", response_class=HTMLResponse)
def mostrar_formulario(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/crear_turno")
def crear_turno(
    nombre: str = Form(...),
    apellido: str = Form(...),
    telefono: str = Form(...),
    fecha: str = Form(...),
    hora: str = Form(...),
    servicio: str = Form(...)
):
    conn = get_connection()
    cursor = conn.cursor()

    # Insertar cliente
    cursor.execute("""
        INSERT INTO clientes (nombre, apellido, telefono)
        VALUES (?, ?, ?)
    """, (nombre, apellido, telefono))

    cliente_id = cursor.lastrowid  # Obtener ID del cliente recién creado

    # Insertar turno con relación al cliente
    cursor.execute("""
        INSERT INTO turnos (cliente_id, fecha, hora, servicio)
        VALUES (?, ?, ?, ?)
    """, (cliente_id, fecha, hora, servicio))

    conn.commit()
    conn.close()

    return {"mensaje": "Turno guardado correctamente"}
