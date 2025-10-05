import random
from datetime import datetime

def calcular_factor_entorno(bacteria, entorno):
    """
    Calcula un factor de ajuste ambiental (0.0 a 1.0)
    según la compatibilidad de la bacteria con las condiciones del entorno.
    """
    # Diferencia entre temperatura del entorno y óptima de la bacteria
    delta_temp = abs(entorno["temperatura"] - bacteria.get("temperatura_optima", 25))
    # Penalización si se aleja más de 20°C
    factor_temp = max(0.0, 1 - (delta_temp / 40))

    # Radiación alta reduce el rendimiento
    factor_radiacion = max(0.1, 1 - entorno["radiacion"] * 0.5)

    # Energía disponible mejora la eficiencia
    factor_energia = min(1.0, entorno["energia_disponible"] / 100)

    # Promedio ponderado de todos los factores
    factor_total = round((factor_temp * 0.5 + factor_radiacion * 0.3 + factor_energia * 0.2), 3)
    return factor_total


def simular_degradacion(bacteria: dict, residuo: dict, entorno: dict, peso_inicial: float):
    """
    Simula la degradación de un residuo considerando la bacteria, el residuo y el entorno.
    """

    eficiencia_base = 0.1
    if "eficiencia" in bacteria and residuo["tipo"] in bacteria["eficiencia"]:
        eficiencia_base = bacteria["eficiencia"][residuo["tipo"]]

    # Calcular factor ambiental
    factor_ambiente = calcular_factor_entorno(bacteria, entorno)

    # Eficiencia total ajustada
    eficiencia_ajustada = round(eficiencia_base * factor_ambiente, 3)

    porcentaje_degradacion = round(eficiencia_ajustada * 100, 2)
    peso_degradado = round(peso_inicial * (porcentaje_degradacion / 100), 2)
    tiempo_estimado = round((30 / (porcentaje_degradacion / 10 + 1)) + random.uniform(-2, 2), 1)

    subproducto = "monómeros reutilizables" if residuo["tipo"] == "plástico" else "compuestos orgánicos"

    resultado = {
    "residuo": residuo["tipo"],
    "bacteria": bacteria["nombre"],
    "entorno": entorno["nombre"],  # 👈 agrega esto
    "eficiencia_ajustada": eficiencia_ajustada,  # 👈 y esto también
    "peso_inicial_g": peso_inicial,
    "porcentaje_degradacion": porcentaje_degradacion,
    "peso_degradado_g": peso_degradado,
    "tiempo_estimado_dias": tiempo_estimado,
    "subproducto": subproducto,
    "fecha_simulacion": datetime.utcnow().isoformat()
}

    return resultado
