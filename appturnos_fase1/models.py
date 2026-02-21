from database import get_connection


# -----------------------------
# CLIENTES
# -----------------------------

def obtener_cliente_por_telefono(telefono):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM clientes WHERE telefono = ?",
        (telefono,)
    )

    cliente = cursor.fetchone()
    conn.close()
    return cliente


def crear_cliente(nombre, telefono):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO clientes (nombre, telefono)
        VALUES (?, ?)
    """, (nombre, telefono))

    conn.commit()
    cliente_id = cursor.lastrowid
    conn.close()

    return cliente_id


# -----------------------------
# SERVICIOS
# -----------------------------

def obtener_servicio(servicio_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM servicios WHERE id = ? AND activo = 1",
        (servicio_id,)
    )

    servicio = cursor.fetchone()
    conn.close()
    return servicio


# -----------------------------
# TURNOS
# -----------------------------

def crear_turno(servicio_id, fecha, hora_inicio, hora_fin):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO turnos (servicio_id, fecha, hora_inicio, hora_fin)
        VALUES (?, ?, ?, ?)
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