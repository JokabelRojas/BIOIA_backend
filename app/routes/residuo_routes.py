from fastapi import APIRouter, HTTPException
from app.schemas.residuo_schema import ResiduoSchema
from app.models.residuo_model import crear_residuo, listar_residuos

router = APIRouter(prefix="/residuos", tags=["Residuos"])

@router.post("/", response_model=dict)
async def crear_residuo_endpoint(residuo: ResiduoSchema):
    try:
        nuevo = await crear_residuo(residuo.dict(by_alias=True))
        return {"message": "Residuo registrado correctamente", "data": nuevo}
    except Exception as e:
        print("Error al crear residuo:", e)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=dict)
async def listar_residuos_endpoint():
    try:
        residuos = await listar_residuos()
        return {"residuos": residuos}
    except Exception as e:
        print("Error al listar residuos:", e)
        raise HTTPException(status_code=500, detail=str(e))
