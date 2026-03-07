from datetime import datetime, timedelta

from appturnos_fase1.models import (
    buscar_cliente,
    crear_cliente,
    obtener_servicio,
    crear_turno,
    vincular_cliente_a_turno
)

from appturnos_fase1.models import verificar_disponibilidad




# =========================
# UTILIDADES
# =========================

def calcular_hora_fin(hora_inicio_str, duracion_minutos):
    formato = "%H:%M"
    hora_inicio = datetime.strptime(hora_inicio_str, formato)
    hora_fin = hora_inicio + timedelta(minutes=duracion_minutos)
    return hora_fin.strftime(formato)



# =========================
# CASO DE USO PRINCIPAL
# =========================

def crear_turno_completo(lista_clientes, servicio_id, fecha, hora_inicio):
    """
    Flujo real de negocio:

    1) Buscar o crear clientes
    2) Obtener servicio
    3) Calcular hora fin
    4) Crear turno (pendiente)
    5) Vincular clientes
    """

    # 1️⃣ Obtener servicio
    servicio = obtener_servicio(servicio_id)

    if not servicio:
        raise ValueError("Servicio no encontrado o inactivo.")

    # 2️⃣ Calcular hora fin
    hora_fin = calcular_hora_fin(hora_inicio, servicio["duracion_minutos"])
    
    # Validar disponibilidad
    disponible = verificar_disponibilidad(fecha, hora_inicio, hora_fin)

    if not disponible:
      raise ValueError("El horario ya está ocupado.")


    # 3️⃣ Crear turno
    turno_id = crear_turno(servicio_id, fecha, hora_inicio, hora_fin)

    # 4️⃣ Procesar clientes
    for cliente in lista_clientes:
        nombre = cliente["nombre"]
        apellido = cliente["apellido"]
        telefono = cliente["telefono"]

        cliente_id = buscar_cliente(nombre, apellido)

        if not cliente_id:
            cliente_id = crear_cliente(nombre, apellido, telefono)

        vincular_cliente_a_turno(turno_id, cliente_id)

    return turno_id

def procesar_turno(nombre, apellido, telefono, servicio_id, fecha, hora_inicio):
    lista_clientes = [{
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono
    }]

    return crear_turno_completo(
        lista_clientes=lista_clientes,
        servicio_id=servicio_id,
        fecha=fecha,
        hora_inicio=hora_inicio
    )