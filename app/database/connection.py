from pymongo import MongoClient
import certifi
from app.config import MONGO_URI, DB_NAME

ca = certifi.where()

try:
    client = MongoClient(
        MONGO_URI,
        tls=True,
        tlsCAFile=ca,
        serverSelectionTimeoutMS=30000,
        connectTimeoutMS=20000,
        socketTimeoutMS=20000,
    )

    # Prueba conexión
    client.admin.command("ping")
    print(f"✅ Conectado exitosamente a MongoDB Atlas: {DB_NAME}")

except Exception as e:
    print("❌ Error de conexión con MongoDB Atlas:", e)

# Base de datos global
database = client[DB_NAME]
