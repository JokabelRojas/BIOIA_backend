from app.database.connection import database
usuario_collection = database["usuarios"]
from bson import ObjectId
from datetime import datetime

def usuario_helper(usuario) -> dict:
    return {
        "id": str(usuario["_id"]),
        "nombre": usuario.get("nombre"),
        "rol": usuario.get("rol"),
        "email": usuario.get("email"),
        "institucion": usuario.get("institucion"),
        "fecha_registro": str(usuario.get("fecha_registro"))
    }

async def crear_usuario(data: dict):
    # Aseguramos que no haya _id en el insert
    if "_id" in data:
        del data["_id"]

    # Convertimos la fecha a datetime si no existe
    if "fecha_registro" not in data:
        data["fecha_registro"] = datetime.utcnow()

    try:
        result = await usuario_collection.insert_one(data)
        nuevo_usuario = await usuario_collection.find_one({"_id": result.inserted_id})
        return usuario_helper(nuevo_usuario)
    except Exception as e:
        print("Error al insertar usuario en MongoDB:", e)
        raise e

async def listar_usuarios():
    usuarios = []
    async for usuario in usuario_collection.find():
        usuarios.append(usuario_helper(usuario))
    return usuarios
