from app.database.connection import database
from bson import ObjectId
from datetime import datetime

simulacion_collection = database.get_collection("simulaciones")

def simulacion_helper(sim) -> dict:
    return {
        "id": str(sim["_id"]),
        "residuo": sim.get("residuo"),
        "bacteria": sim.get("bacteria"),
        "entorno": sim.get("entorno"),  # 👈 agrega esto
        "eficiencia_ajustada": sim.get("eficiencia_ajustada"),  # 👈 y esto
        "peso_inicial_g": sim.get("peso_inicial_g"),
        "porcentaje_degradacion": sim.get("porcentaje_degradacion"),
        "peso_degradado_g": sim.get("peso_degradado_g"),
        "tiempo_estimado_dias": sim.get("tiempo_estimado_dias"),
        "subproducto": sim.get("subproducto"),
        "fecha_simulacion": str(sim.get("fecha_simulacion"))
    }


async def guardar_simulacion(resultado: dict):
    if "_id" in resultado:
        del resultado["_id"]
    if "fecha_simulacion" not in resultado:
        resultado["fecha_simulacion"] = datetime.utcnow()

    nueva = await simulacion_collection.insert_one(resultado)
    sim = await simulacion_collection.find_one({"_id": nueva.inserted_id})
    return simulacion_helper(sim)

async def listar_simulaciones():
    simulaciones = []
    for sim in simulacion_collection.find():  # 👈 corregido
        simulaciones.append(simulacion_helper(sim))
    return simulaciones

