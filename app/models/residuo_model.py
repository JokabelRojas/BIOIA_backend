from app.database.connection import database
from bson import ObjectId
from datetime import datetime

residuo_collection = database.get_collection("residuos")

def residuo_helper(residuo) -> dict:
    return {
        "id": str(residuo["_id"]),
        "tipo": residuo.get("tipo"),
        "categoria": residuo.get("categoria"),
        "descripcion": residuo.get("descripcion"),
        "densidad": residuo.get("densidad"),
        "toxicidad": residuo.get("toxicidad"),
        "origen": residuo.get("origen"),
        "fecha_registro": str(residuo.get("fecha_registro"))
    }

async def crear_residuo(data: dict):
    if "_id" in data:
        del data["_id"]
    if "fecha_registro" not in data:
        data["fecha_registro"] = datetime.utcnow()
    nuevo = await residuo_collection.insert_one(data)
    res = await residuo_collection.find_one({"_id": nuevo.inserted_id})
    return residuo_helper(res)

async def listar_residuos():
    residuos = []
    async for res in residuo_collection.find():
        residuos.append(residuo_helper(res))
    return residuos
