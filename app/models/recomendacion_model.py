from app.database.connection import database
from bson import ObjectId
from datetime import datetime

recomendacion_collection = database.get_collection("recomendaciones")

def recomendacion_helper(rec) -> dict:
    return {
        "id": str(rec["_id"]),
        "simulacion_id": rec.get("simulacion_id"),
        "tipo_residuo": rec.get("tipo_residuo"),
        "bacteria_sugerida": rec.get("bacteria_sugerida"),
        "observaciones": rec.get("observaciones"),
        "eficiencia_predicha": rec.get("eficiencia_predicha"),
        "fecha_generada": str(rec.get("fecha_generada"))
    }

async def crear_recomendacion(data: dict):
    if "_id" in data:
        del data["_id"]
    if "fecha_generada" not in data:
        data["fecha_generada"] = datetime.utcnow()
    nueva = await recomendacion_collection.insert_one(data)
    rec = await recomendacion_collection.find_one({"_id": nueva.inserted_id})
    return recomendacion_helper(rec)

async def listar_recomendaciones():
    recs = []
    async for r in recomendacion_collection.find():
        recs.append(recomendacion_helper(r))
    return recs
