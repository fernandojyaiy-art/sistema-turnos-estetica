from appturnos_fase1.database import get_connection


# =========================
# CLIENTES
# =========================

def buscar_cliente(nombre, apellido):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id FROM clientes
        WHERE nombre = ? AND apellido = ?
    """, (nombre, apellido))

    cliente = cursor.fetchone()
    conn.close()

    return cliente[0] if cliente else None


def crear_cliente(nombre, apellido, telefono):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO clientes (nombre, apellido, telefono)
        VALUES (?, ?, ?)
    """, (nombre, apellido, telefono))

    conn.commit()
    cliente_id = cursor.lastrowid
    conn.close()

    return cliente_id


# =========================
# SERVICIOS
# =========================

def obtener_servicio(servicio_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nombre, duracion_minutos
        FROM servicios
        WHERE id = ? AND activo = 1
    """, (servicio_id,))

    servicio = cursor.fetchone()
    conn.close()

    if servicio:
        return {
            "id": servicio[0],
            "nombre": servicio[1],
            "duracion_minutos": servicio[2]
        }
    return None


# =========================
# TURNOS
# =========================

def crear_turno(servicio_id, fecha, hora_inicio, hora_fin):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO turnos (servicio_id, fecha, hora_inicio, hora_fin, estado)
        VALUES (?, ?, ?, ?, 'pendiente')
    """, (servicio_id, fecha, hora_inicio, hora_fin))

    conn.commit()
    turno_id = cursor.lastrowid
    conn.close()

    return turno_id


def vincular_cliente_a_turno(turno_id, cliente_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO turno_clientes (turno_id, cliente_id)
        VALUES (?, ?)
    """, (turno_id, cliente_id))

    conn.commit()
    conn.close()

   # =========================
# DISPONIBILIDAD
# =========================

def verificar_disponibilidad(fecha, hora_inicio, hora_fin):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id FROM turnos
        WHERE fecha = ?
       
        AND (
            hora_inicio < ?
            AND hora_fin > ?
        )
    """, (fecha, hora_fin, hora_inicio))

    conflicto = cursor.fetchone()
    conn.close()

    return conflicto is None

def listar_servicios_activos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nombre, precio
        FROM servicios
        WHERE activo = 1
    """)

    servicios = cursor.fetchall()
    conn.close()

    return [
        {
            "id": s[0],
            "nombre": s[1],
            "precio": s[2]
        }
        for s in servicios
    ]

def listar_turnos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            t.id,
            t.fecha,
            t.hora_inicio,
            t.hora_fin,
            t.estado,
            s.nombre AS servicio,
            c.nombre || ' ' || c.apellido AS cliente
        FROM turnos t
        JOIN servicios s ON t.servicio_id = s.id
        JOIN turno_clientes tc ON tc.turno_id = t.id
        JOIN clientes c ON c.id = tc.cliente_id
        ORDER BY t.fecha, t.hora_inicio
    """)

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": r[0],
            "fecha": r[1],
            "hora_inicio": r[2],
            "hora_fin": r[3],
            "estado": r[4],
            "servicio": r[5],
            "cliente": r[6]
        }
        for r in rows
    ]