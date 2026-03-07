# =========================
# IMPORTS
# =========================

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from appturnos_fase1.database import create_tables, seed_servicios
from appturnos_fase1.logic import procesar_turno
from appturnos_fase1.models import listar_servicios_activos 
from appturnos_fase1.models import listar_turnos

from fastapi.responses import RedirectResponse

# =========================
# INICIALIZACIÓN BASE DE DATOS
# =========================

create_tables()
seed_servicios()


# =========================
# CONFIGURACIÓN APP
# =========================

app = FastAPI()
templates = Jinja2Templates(directory="appturnos_fase1/templates")


# =========================
# RUTA FORMULARIO
# =========================

@app.get("/", response_class=HTMLResponse)
def mostrar_formulario(request: Request):

    servicios = listar_servicios_activos()

    return templates.TemplateResponse(
        "crear_turno.html",
        {
            "request": request,
            "servicios": servicios
        }
    )


# =========================
# RUTA CREAR TURNO
# =========================

@app.post("/crear_turno")
def crear_turno(
    nombre: str = Form(...),
    apellido: str = Form(...),
    telefono: str = Form(...),
    servicio_id: int = Form(...),
    fecha: str = Form(...),
    hora_inicio: str = Form(...)
):
    try:
        turno_id = procesar_turno(
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            servicio_id=servicio_id,
            fecha=fecha,
            hora_inicio=hora_inicio
        )


        return RedirectResponse(url="/turnos?mensaje=ok", status_code=303) 
    
    except ValueError:
        
        return RedirectResponse(url="/?mensaje=ocupado", status_code=303)


# =========================
# RUTAS ADICIONALES PARA VER SERVICIOS Y TURNOS
# =========================

@app.get("/servicios", response_class=HTMLResponse)
def mostrar_servicios(request: Request):

    servicios = listar_servicios_activos()

    return templates.TemplateResponse(
        "servicios.html",
        {
            "request": request,
            "servicios": servicios
        }
    )

@app.get("/turnos", response_class=HTMLResponse)
def ver_turnos(request: Request):
    turnos = listar_turnos()
    return templates.TemplateResponse(
        "turnos.html",
        {
            "request": request,
            "turnos": turnos
        }
    )