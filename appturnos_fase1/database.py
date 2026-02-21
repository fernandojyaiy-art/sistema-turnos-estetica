import sqlite3


DB_NAME = "turnos_fase1.db"


def get_connection():
    """
    Crea y devuelve una conexión a la base de datos.
    Activa foreign keys para respetar relaciones.
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def create_tables():
    """
    Crea todas las tablas necesarias para Fase 1.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # -----------------------------
    # TABLA CLIENTES
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT
        )
    """)

    # -----------------------------
    # TABLA SERVICIOS
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS servicios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            duracion_minutos INTEGER NOT NULL,
            camillas_requeridas INTEGER NOT NULL,
            precio REAL,
            activo INTEGER DEFAULT 1
        )
    """)

    # -----------------------------
    # TABLA TURNOS
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS turnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            servicio_id INTEGER NOT NULL,
            fecha TEXT NOT NULL,
            hora_inicio TEXT NOT NULL,
            hora_fin TEXT NOT NULL,
            estado TEXT DEFAULT 'pendiente',
            FOREIGN KEY (servicio_id) REFERENCES servicios(id)
        )
    """)

    # -----------------------------
    # TABLA TURNO_CLIENTES
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS turno_clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turno_id INTEGER NOT NULL,
            cliente_id INTEGER NOT NULL,
            FOREIGN KEY (turno_id) REFERENCES turnos(id) ON DELETE CASCADE,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()


def seed_servicios():
    """
    Inserta servicios base solo si la tabla está vacía.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Verificar si ya existen servicios
    cursor.execute("SELECT COUNT(*) FROM servicios")
    cantidad = cursor.fetchone()[0]

    if cantidad == 0:
        print("Insertando servicios base...")

        servicios_base = [
            ("Limpieza facial profunda", 60, 1, 15000, 1),
            ("Rostro cuello y escote", 90, 1, 22000, 1),
            ("Promo 2 limpiezas faciales", 60, 2, 25000, 1),
        ]

        cursor.executemany("""
            INSERT INTO servicios 
            (nombre, duracion_minutos, camillas_requeridas, precio, activo)
            VALUES (?, ?, ?, ?, ?)
        """, servicios_base)

        conn.commit()
        print("Servicios insertados correctamente.")
    else:
        print("Los servicios ya existen. No se insertó nada.")

    conn.close()