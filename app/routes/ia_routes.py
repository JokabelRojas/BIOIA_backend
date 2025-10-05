from fastapi import APIRouter, HTTPException
from app.services.ia_model import entrenar_modelo_bioai

router = APIRouter(prefix="/ia", tags=["Inteligencia Artificial BioAI"])

@router.post("/entrenar", response_model=dict)
async def entrenar_modelo_endpoint():
    """
    Entrena el modelo de IA con las simulaciones almacenadas en la base de datos.
    """
    try:
        resultado = await entrenar_modelo_bioai()
        return resultado
    except Exception as e:
        print("❌ Error al entrenar IA:", e)
        raise HTTPException(status_code=500, detail=str(e))
