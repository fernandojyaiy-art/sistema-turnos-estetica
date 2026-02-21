from datetime import datetime, timedelta
from models import (
    obtener_cliente_por_telefono,
    crear_cliente,
    obtener_servicio,
    crear_turno,
    vincular_cliente_a_turno
)


def calcular_hora_fin(hora_inicio_str, duracion_minutos):
    """
    Calcula la hora de finalización sumando la duración del servicio.
    """
    formato = "%H:%M"
    hora_inicio = datetime.strptime(hora_inicio_str, formato)
    hora_fin = hora_inicio + timedelta(minutes=duracion_minutos)
    return hora_fin.strftime(formato)


def crear_turno_completo(lista_clientes, servicio_id, fecha, hora_inicio):
    """
    Crea un turno completo:
    - Obtiene servicio
    - Calcula hora_fin
    - Crea turno
    - Vincula clientes
    """

    servicio = obtener_servicio(servicio_id)

    if not servicio:
        raise ValueError("Servicio no encontrado o inactivo.")

    # Calcular hora fin automáticamente
    hora_fin = calcular_hora_fin(hora_inicio, servicio["duracion_minutos"])

    # Crear turno
    turno_id = crear_turno(servicio_id, fecha, hora_inicio, hora_fin)

    # Vincular clientes
    for cliente in lista_clientes:
        telefono = cliente["telefono"]
        nombre = cliente["nombre"]

        cliente_existente = obtener_cliente_por_telefono(telefono)

        if cliente_existente:
            cliente_id = cliente_existente["id"]
        else:
            cliente_id = crear_cliente(nombre, telefono)

        vincular_cliente_a_turno(turno_id, cliente_id)

    return turno_id