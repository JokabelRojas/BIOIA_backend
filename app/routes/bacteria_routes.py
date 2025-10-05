from fastapi import APIRouter, HTTPException
from app.schemas.bacteria_schema import BacteriaSchema
from app.models.bacteria_model import crear_bacteria, listar_bacterias

router = APIRouter(prefix="/bacterias", tags=["Bacterias"])

@router.post("/", response_model=dict)
async def crear_bacteria_endpoint(bacteria: BacteriaSchema):
    try:
        nueva = await crear_bacteria(bacteria.dict(by_alias=True))
        return {"message": "Bacteria registrada correctamente", "data": nueva}
    except Exception as e:
        print("Error al crear bacteria:", e)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=dict)
async def listar_bacterias_endpoint():
    try:
        bacterias = await listar_bacterias()
        return {"bacterias": bacterias}
    except Exception as e:
        print("Error al listar bacterias:", e)
        raise HTTPException(status_code=500, detail=str(e))
