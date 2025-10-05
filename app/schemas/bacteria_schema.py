from pydantic import BaseModel, Field
from typing import Optional, Dict
from datetime import datetime

class BacteriaSchema(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    nombre: str = Field(..., example="Ideonella sakaiensis")
    descripcion: Optional[str] = Field(None, example="Bacteria que degrada plásticos PET")
    eficiencia: Dict[str, float] = Field(..., example={"plástico": 0.35, "textil": 0.05})
    temperatura_optima: float = Field(..., example=30.0)
    ph_optimo: float = Field(..., example=7.0)
    radiacion_resistencia: float = Field(..., example=0.4)
    tipo_entorno: Optional[str] = Field("terrestre", example="marciano")
    fecha_registro: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Ideonella sakaiensis",
                "descripcion": "Degrada plásticos PET en monómeros reutilizables",
                "eficiencia": {"plástico": 0.35, "textil": 0.05},
                "temperatura_optima": 30.0,
                "ph_optimo": 7.0,
                "radiacion_resistencia": 0.4,
                "tipo_entorno": "terrestre"
            }
        }
