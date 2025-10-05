from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class EntornoSchema(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    nombre: str = Field(..., example="Módulo Biológico Ares")
    ubicacion: str = Field(..., example="Base Marciana - Sector 3")
    temperatura: float = Field(..., example=-40.0)
    radiacion: float = Field(..., example=0.8)
    energia_disponible: float = Field(..., example=120.5)
    tipo_entorno: str = Field(..., example="marciano")
    fecha_registro: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Módulo Biológico Ares",
                "ubicacion": "Base Marciana - Sector 3",
                "temperatura": -40.0,
                "radiacion": 0.8,
                "energia_disponible": 120.5,
                "tipo_entorno": "marciano"
            }
        }
