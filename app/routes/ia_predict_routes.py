from fastapi import APIRouter, HTTPException
from app.services.ia_predict import predecir_degradacion

router = APIRouter(prefix="/ia", tags=["Inteligencia Artificial BioAI"])

@router.post("/prediccion", response_model=dict)
async def predecir_endpoint(residuo: dict):
    """
    Predice el porcentaje de degradación usando el modelo de IA entrenado.
    """
    try:
        resultado = await predecir_degradacion(residuo)
        return resultado
    except Exception as e:
        print("❌ Error en predicción:", e)
        raise HTTPException(status_code=500, detail=str(e))
