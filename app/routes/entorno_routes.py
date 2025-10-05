from fastapi import APIRouter, HTTPException
from app.schemas.entorno_schema import EntornoSchema
from app.models.entorno_model import crear_entorno, listar_entornos

router = APIRouter(prefix="/entornos", tags=["Entornos"])

@router.post("/", response_model=dict)
async def crear_entorno_endpoint(entorno: EntornoSchema):
    try:
        nuevo = await crear_entorno(entorno.dict(by_alias=True))
        return {"message": "Entorno registrado correctamente", "data": nuevo}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=dict)
async def listar_entornos_endpoint():
    try:
        entornos = await listar_entornos()
        return {"entornos": entornos}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
