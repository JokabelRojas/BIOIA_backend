from app.database.connection import database
from bson import ObjectId
from datetime import datetime

entorno_collection = database.get_collection("entornos")

def entorno_helper(entorno) -> dict:
    return {
        "id": str(entorno["_id"]),
        "nombre": entorno.get("nombre"),
        "ubicacion": entorno.get("ubicacion"),
        "temperatura": entorno.get("temperatura"),
        "radiacion": entorno.get("radiacion"),
        "energia_disponible": entorno.get("energia_disponible"),
        "tipo_entorno": entorno.get("tipo_entorno"),
        "fecha_registro": str(entorno.get("fecha_registro"))
    }

async def crear_entorno(data: dict):
    if "_id" in data:
        del data["_id"]
    if "fecha_registro" not in data:
        data["fecha_registro"] = datetime.utcnow()
    nuevo = await entorno_collection.insert_one(data)
    res = await entorno_collection.find_one({"_id": nuevo.inserted_id})
    return entorno_helper(res)

async def listar_entornos():
    entornos = []
    async for e in entorno_collection.find():
        entornos.append(entorno_helper(e))
    return entornos
