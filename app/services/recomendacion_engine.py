from statistics import mean
from app.models.simulacion_model import listar_simulaciones
from app.models.recomendacion_model import crear_recomendacion

async def generar_recomendaciones():
    """
    Analiza las simulaciones guardadas y genera recomendaciones
    basadas en el desempeño histórico de las bacterias.
    """
    simulaciones = await listar_simulaciones()
    if not simulaciones:
        return {"message": "No hay simulaciones suficientes para generar recomendaciones."}

    # Agrupar simulaciones por tipo de residuo
    agrupadas = {}
    for sim in simulaciones:
        tipo = sim["residuo"]
        if tipo not in agrupadas:
            agrupadas[tipo] = []
        agrupadas[tipo].append(sim)

    recomendaciones_creadas = []

    # Calcular promedios por bacteria
    for tipo_residuo, lista in agrupadas.items():
        resumen = {}
        for sim in lista:
            bacteria = sim["bacteria"]
            if bacteria not in resumen:
                resumen[bacteria] = []
            resumen[bacteria].append(sim["porcentaje_degradacion"])

        # Elegir la bacteria con mejor rendimiento promedio
        mejor_bacteria = max(resumen, key=lambda b: mean(resumen[b]))
        mejor_eficiencia = round(mean(resumen[mejor_bacteria]) / 100, 3)

        # Crear recomendación en MongoDB
        rec_data = {
            "tipo_residuo": tipo_residuo,
            "bacteria_sugerida": mejor_bacteria,
            "observaciones": f"Bacteria con mejor rendimiento histórico para {tipo_residuo}",
            "eficiencia_predicha": mejor_eficiencia
        }

        rec = await crear_recomendacion(rec_data)
        recomendaciones_creadas.append(rec)

    return {
        "message": "Recomendaciones generadas exitosamente.",
        "recomendaciones": recomendaciones_creadas
    }
