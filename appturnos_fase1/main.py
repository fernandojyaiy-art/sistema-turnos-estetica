

##from database import create_tables, seed_servicios

##if __name__ == "__main__":
##  create_tables()
##  seed_servicios()
##  print("Base de datos Fase 1 lista.") ##

from database import create_tables, seed_servicios
from logic import crear_turno_completo

if __name__ == "__main__":
    create_tables()
    seed_servicios()

    clientes = [
        {"nombre": "Ana", "telefono": "111"},
        {"nombre": "Maria", "telefono": "222"}
    ]

    turno_id = crear_turno_completo(
        lista_clientes=clientes,
        servicio_id=3,  # Promo 2 limpiezas
        fecha="2026-03-01",
        hora_inicio="10:00"
    )

    print("Turno creado con ID:", turno_id)