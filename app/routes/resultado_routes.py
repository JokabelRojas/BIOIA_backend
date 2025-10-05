from fastapi import APIRouter, HTTPException
from app.models.resultado_model import guardar_resultado, listar_resultados

router = APIRouter(prefix="/resultados", tags=["Resultados BioAI"])

@router.post("/", response_model=dict)
async def crear_resultado_endpoint(resultado: dict):
    try:
        nuevo = await guardar_resultado(resultado)
        return {"message": "Resultado guardado correctamente", "data": nuevo}
    except Exception as e:
        print("❌ Error al guardar resultado:", e)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=dict)
async def listar_resultados_endpoint():
    try:
        resultados = await listar_resultados()
        return {"resultados": resultados}
    except Exception as e:
        print("❌ Error al listar resultados:", e)
        raise HTTPException(status_code=500, detail=str(e))
