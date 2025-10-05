from app.database.connection import database
from bson import ObjectId
from datetime import datetime

resultado_collection = database.get_collection("resultados")

def resultado_helper(resultado) -> dict:
    return {
        "id": str(resultado["_id"]),
        "simulacion_id": resultado.get("simulacion_id"),
        "bacteria": resultado.get("bacteria"),
        "residuo": resultado.get("residuo"),
        "entorno": resultado.get("entorno"),
        "porcentaje_degradacion": resultado.get("porcentaje_degradacion"),
        "energia_usada": resultado.get("energia_usada"),
        "eficiencia_final": resultado.get("eficiencia_final"),
        "tiempo_estimado_dias": resultado.get("tiempo_estimado_dias"),
        "fecha_registro": str(resultado.get("fecha_registro"))
    }

async def guardar_resultado(data: dict):
    if "_id" in data:
        del data["_id"]
    if "fecha_registro" not in data:
        data["fecha_registro"] = datetime.utcnow()
    nuevo = await resultado_collection.insert_one(data)
    res = await resultado_collection.find_one({"_id": nuevo.inserted_id})
    return resultado_helper(res)

async def listar_resultados():
    resultados = []
    for r in resultado_collection.find():  # 👈 ← for normal, no async for
        resultados.append(resultado_helper(r))
    return resultados

