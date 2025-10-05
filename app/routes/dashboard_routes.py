from fastapi import APIRouter, HTTPException
from app.services.dashboard_bioai import generar_dashboard_bioai

router = APIRouter(prefix="/dashboard", tags=["Dashboard BioAI"])

@router.get("/", response_model=dict)
async def ver_dashboard():
    """
    Genera y devuelve métricas y gráficos del sistema BioAI.
    """
    try:
        resultado = await generar_dashboard_bioai()
        return resultado
    except Exception as e:
        print("❌ Error al generar dashboard:", e)
        raise HTTPException(status_code=500, detail=str(e))
