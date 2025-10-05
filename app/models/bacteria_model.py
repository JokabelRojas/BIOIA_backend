from app.database.connection import database
from bson import ObjectId
from datetime import datetime

bacteria_collection = database.get_collection("bacterias")

def bacteria_helper(bacteria) -> dict:
    return {
        "id": str(bacteria["_id"]),
        "nombre": bacteria.get("nombre"),
        "descripcion": bacteria.get("descripcion"),
        "eficiencia": bacteria.get("eficiencia"),
        "temperatura_optima": bacteria.get("temperatura_optima"),
        "ph_optimo": bacteria.get("ph_optimo"),
        "radiacion_resistencia": bacteria.get("radiacion_resistencia"),
        "tipo_entorno": bacteria.get("tipo_entorno"),
        "fecha_registro": str(bacteria.get("fecha_registro"))
    }

async def crear_bacteria(data: dict):
    if "_id" in data:
        del data["_id"]
    if "fecha_registro" not in data:
        data["fecha_registro"] = datetime.utcnow()
    nueva = await bacteria_collection.insert_one(data)
    bact = await bacteria_collection.find_one({"_id": nueva.inserted_id})
    return bacteria_helper(bact)

async def listar_bacterias():
    bacterias = []
    async for b in bacteria_collection.find():
        bacterias.append(bacteria_helper(b))
    return bacterias
