from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class UsuarioSchema(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    nombre: str = Field(..., min_length=3, max_length=100)
    rol: str
    email: EmailStr
    institucion: Optional[str] = None
    fecha_registro: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Jokabel Rojas",
                "rol": "Investigadora IA",
                "email": "jokabel@bioai.org",
                "institucion": "Astrocoders Lab"
            }
        }
