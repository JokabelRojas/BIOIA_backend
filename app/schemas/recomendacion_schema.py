from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class RecomendacionSchema(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    simulacion_id: Optional[str] = None
    tipo_residuo: str = Field(..., example="plástico")
    bacteria_sugerida: str = Field(..., example="Ideonella sakaiensis")
    observaciones: str = Field(..., example="Alta eficiencia y resistencia en condiciones frías")
    eficiencia_predicha: float = Field(..., example=0.35)
    fecha_generada: datetime = Field(default_factory=datetime.utcnow)
