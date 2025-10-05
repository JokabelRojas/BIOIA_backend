from fastapi import APIRouter, HTTPException
from app.services.recomendacion_engine import generar_recomendaciones
from app.models.recomendacion_model import listar_recomendaciones

router = APIRouter(prefix="/recomendar", tags=["Recomendaciones"])

@router.post("/", response_model=dict)
async def generar_recomendaciones_endpoint():
    """
    Genera recomendaciones basadas en las simulaciones históricas.
    """
    try:
        resultado = await generar_recomendaciones()
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=dict)
async def listar_recomendaciones_endpoint():
    """
    Muestra todas las recomendaciones registradas.
    """
    try:
        recs = await listar_recomendaciones()
        return {"recomendaciones": recs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
