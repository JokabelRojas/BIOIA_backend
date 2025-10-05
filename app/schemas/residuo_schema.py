from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ResiduoSchema(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    tipo: str = Field(..., example="plástico")
    categoria: str = Field(..., example="PET")
    descripcion: Optional[str] = Field(None, example="Residuos plásticos de envases PET")
    densidad: Optional[float] = Field(None, example=1.38)
    toxicidad: Optional[float] = Field(None, example=0.2)
    origen: Optional[str] = Field(None, example="urbano")
    fecha_registro: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "tipo": "plástico",
                "categoria": "PET",
                "descripcion": "Residuos plásticos transparentes de botellas",
                "densidad": 1.38,
                "toxicidad": 0.2,
                "origen": "urbano"
            }
        }
