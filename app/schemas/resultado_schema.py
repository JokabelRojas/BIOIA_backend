from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ResultadoSchema(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    simulacion_id: Optional[str] = None
    indicador: str = Field(..., example="Energía utilizada")
    valor: float = Field(..., example=25.7)
    unidad: str = Field(..., example="kWh")
    interpretacion: str = Field(..., example="Consumo moderado durante la degradación")
    fecha_registro: datetime = Field(default_factory=datetime.utcnow)
