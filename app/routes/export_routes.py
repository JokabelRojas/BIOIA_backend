from fastapi import APIRouter, Query, HTTPException
from app.services.export_bioai import exportar_datos_bioai

router = APIRouter(prefix="/exportar", tags=["Exportar BioAI"])

@router.get("/", response_model=dict)
async def exportar_datos(formato: str = Query("excel", enum=["excel", "csv"])):
    """
    Exporta los datos del sistema BioAI en formato Excel o CSV.
    Retorna el archivo codificado en base64.
    """
    try:
        resultado = await exportar_datos_bioai(formato)
        return resultado
    except Exception as e:
        print("❌ Error al exportar datos:", e)
        raise HTTPException(status_code=500, detail=str(e))
