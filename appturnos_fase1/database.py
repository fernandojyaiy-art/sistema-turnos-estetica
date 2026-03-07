import sqlite3

DB_NAME = "turnos.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # ==========================
    # TABLA CLIENTES
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        telefono TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # ==========================
    # TABLA SERVICIOS
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS servicios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    duracion_minutos INTEGER NOT NULL,
    precio REAL NOT NULL,
    activo INTEGER DEFAULT 1
)
    """)

    # ==========================
    # TABLA TURNOS
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS turnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        servicio_id INTEGER NOT NULL,
        fecha DATE NOT NULL,
        hora_inicio TIME NOT NULL,
        hora_fin TIME NOT NULL,
        estado TEXT DEFAULT 'pendiente',
        FOREIGN KEY (servicio_id) REFERENCES servicios(id)
    )
    """)

    # ==========================
    # RELACION MUCHOS A MUCHOS
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS turno_clientes (
        turno_id INTEGER,
        cliente_id INTEGER,
        PRIMARY KEY (turno_id, cliente_id),
        FOREIGN KEY (turno_id) REFERENCES turnos(id),
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
    """)

    conn.commit()
    conn.close()
   
def seed_servicios():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM servicios")
    count = cursor.fetchone()[0]

    if count == 0:
        servicios = [
            ("Limpieza Facial", 15000, 60, 1),
            ("Peeling", 12000, 45, 1),
            ("Promo 2 personas", 25000, 90, 1),
            ("Tratamiento antiage", 18000, 75, 1),
            ("Dermaplaning", 16000, 60, 1),
            ("Radiofrecuencia", 20000, 80, 1),
            ("Higiene profunda", 17000, 70, 1),
            # Agregá todos los que estén en serv.html
        ]

        cursor.executemany("""
            INSERT INTO servicios (nombre, precio, duracion_minutos, activo)
            VALUES (?, ?, ?, ?)
        """, servicios)

    conn.commit()
    conn.close()