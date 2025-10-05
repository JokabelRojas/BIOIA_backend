import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from app.models.resultado_model import listar_resultados

async def generar_dashboard_bioai():
    """
    Genera un resumen gráfico del desempeño del sistema BioAI.
    Devuelve estadísticas y gráficos codificados en base64.
    """
    resultados = await listar_resultados()
    if not resultados:
        return {"message": "No hay resultados suficientes para generar el dashboard."}

    # Convertir los resultados a DataFrame
    df = pd.DataFrame(resultados)

    # Calcular métricas generales
    promedio_degradacion = round(df["porcentaje_degradacion"].mean(), 2)
    promedio_energia = round(df["energia_usada"].mean(), 2)
    promedio_eficiencia = round(df["eficiencia_final"].mean() * 100, 2)

    # --- Gráfico 1: Degradación promedio por bacteria ---
    grafico1 = BytesIO()
    degradacion_bacterias = df.groupby("bacteria")["porcentaje_degradacion"].mean().sort_values(ascending=False)
    degradacion_bacterias.plot(kind="bar", color="#33B864", title="Degradación Promedio por Bacteria")
    plt.ylabel("% Degradación")
    plt.tight_layout()
    plt.savefig(grafico1, format="png")
    plt.close()
    grafico1_base64 = base64.b64encode(grafico1.getvalue()).decode("utf-8")

    # --- Gráfico 2: Energía usada por entorno ---
    grafico2 = BytesIO()
    energia_entornos = df.groupby("entorno")["energia_usada"].mean()
    energia_entornos.plot(kind="bar", color="#1E90FF", title="Energía Promedio por Entorno")
    plt.ylabel("Energía usada (unidades)")
    plt.tight_layout()
    plt.savefig(grafico2, format="png")
    plt.close()
    grafico2_base64 = base64.b64encode(grafico2.getvalue()).decode("utf-8")

    # --- Gráfico 3: Eficiencia final promedio ---
    grafico3 = BytesIO()
    eficiencia_bacterias = df.groupby("bacteria")["eficiencia_final"].mean() * 100
    eficiencia_bacterias.plot(kind="bar", color="#FFA500", title="Eficiencia Final Promedio (%)")
    plt.ylabel("% Eficiencia")
    plt.tight_layout()
    plt.savefig(grafico3, format="png")
    plt.close()
    grafico3_base64 = base64.b64encode(grafico3.getvalue()).decode("utf-8")

    # Devolver métricas + gráficos en base64 (para mostrar en frontend o guardar)
    return {
        "resumen": {
            "promedio_degradacion": promedio_degradacion,
            "promedio_energia": promedio_energia,
            "promedio_eficiencia": promedio_eficiencia
        },
        "graficos": {
            "degradacion_bacterias": grafico1_base64,
            "energia_entornos": grafico2_base64,
            "eficiencia_bacterias": grafico3_base64
        }
    }
