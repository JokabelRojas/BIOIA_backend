from fastapi import APIRouter, HTTPException
from app.services.bioai_engine import simular_degradacion
from app.models.simulacion_model import guardar_simulacion, listar_simulaciones
from app.models.bacteria_model import listar_bacterias
from app.models.entorno_model import listar_entornos
from app.models.resultado_model import guardar_resultado  # ✅ Importación añadida

router = APIRouter(prefix="/simular", tags=["Simulación BioAI"])


@router.post("/", response_model=dict)
async def simular_residuo(residuo: dict):
    """
    Ejecuta la simulación BioAI considerando bacterias, residuos y entornos.
    Además, guarda automáticamente los resultados (energía y eficiencia).
    """
    try:
        tipo_residuo = residuo.get("tipo", "plástico")

        # 🧫 Buscar bacterias registradas
        bacterias = await listar_bacterias()
        if not bacterias:
            raise HTTPException(status_code=404, detail="No hay bacterias registradas.")

        # 🌌 Buscar entornos registrados
        entornos = await listar_entornos()
        if not entornos:
            raise HTTPException(status_code=404, detail="No hay entornos registrados.")

        # Seleccionar entorno y bacteria más eficiente
        entorno = entornos[0]
        mejor_bacteria = max(bacterias, key=lambda b: b["eficiencia"].get(tipo_residuo, 0))

        # 🧠 Ejecutar simulación
        resultado = simular_degradacion(
            mejor_bacteria,
            residuo,
            entorno,
            peso_inicial=residuo.get("peso_inicial", 500)
        )

        # 💾 Guardar simulación principal
        guardado = await guardar_simulacion(resultado)

        # 🔹 Calcular energía y eficiencia final (simulada)
        energia_usada = round(resultado["peso_inicial_g"] * resultado["eficiencia_ajustada"] * 0.5, 2)
        eficiencia_final = round(resultado["porcentaje_degradacion"] / 100, 3)

        # 💾 Guardar resultado completo
        await guardar_resultado({
            "simulacion_id": guardado["id"],
            "bacteria": resultado["bacteria"],
            "residuo": resultado["residuo"],
            "entorno": resultado["entorno"],
            "porcentaje_degradacion": resultado["porcentaje_degradacion"],
            "energia_usada": energia_usada,
            "eficiencia_final": eficiencia_final,
            "tiempo_estimado_dias": resultado["tiempo_estimado_dias"]
        })

        return {
            "message": f"Simulación realizada con {mejor_bacteria['nombre']} en {entorno['nombre']}",
            "data": guardado
        }

    except Exception as e:
        print("❌ Error en simulación:", e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/", response_model=dict)
async def listar_todas_las_simulaciones():
    """
    Lista todas las simulaciones almacenadas.
    """
    try:
        simulaciones = await listar_simulaciones()
        return {"simulaciones": simulaciones}
    except Exception as e:
        print("❌ Error al listar simulaciones:", e)
        raise HTTPException(status_code=500, detail=str(e))
