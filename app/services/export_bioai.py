import pandas as pd
from io import BytesIO
import base64
from app.models.resultado_model import listar_resultados
from app.models.simulacion_model import listar_simulaciones

async def exportar_datos_bioai(formato: str = "excel"):
    """
    Exporta los datos del sistema BioAI (simulaciones + resultados)
    a Excel o CSV y devuelve el archivo codificado en base64.
    """
    simulaciones = await listar_simulaciones()
    resultados = await listar_resultados()

    if not simulaciones and not resultados:
        return {"message": "No hay datos para exportar."}

    # Crear DataFrames
    df_sim = pd.DataFrame(simulaciones)
    df_res = pd.DataFrame(resultados)

    # Limpiar IDs redundantes
    for df in [df_sim, df_res]:
        if "_id" in df.columns:
            df.drop("_id", axis=1, inplace=True)

    # Guardar en memoria
    buffer = BytesIO()

    if formato == "excel":
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df_sim.to_excel(writer, index=False, sheet_name="Simulaciones")
            df_res.to_excel(writer, index=False, sheet_name="Resultados")
    elif formato == "csv":
        df_sim.to_csv(buffer, index=False)
        df_res.to_csv(buffer, index=False)
    else:
        return {"message": "Formato no válido. Usa 'excel' o 'csv'."}

    # Convertir a Base64
    buffer.seek(0)
    data_base64 = base64.b64encode(buffer.read()).decode("utf-8")

    return {
        "message": f"Datos exportados correctamente en formato {formato}.",
        "archivo_base64": data_base64
    }
