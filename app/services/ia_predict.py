import numpy as np
from sklearn.linear_model import LinearRegression
from app.models.simulacion_model import listar_simulaciones

async def predecir_degradacion(residuo: dict):
    """
    Usa un modelo entrenado simple de regresión lineal
    para predecir el porcentaje de degradación basado en datos existentes.
    """
    simulaciones = await listar_simulaciones()
    if not simulaciones:
        return {"message": "No hay datos suficientes para predecir."}

    # Entrenar modelo rápido con los datos existentes
    X = np.array([[s.get("peso_inicial_g", 0),
                   s.get("eficiencia_ajustada", 0),
                   s.get("tiempo_estimado_dias", 0)] for s in simulaciones])
    y = np.array([s.get("porcentaje_degradacion", 0) for s in simulaciones])

    modelo = LinearRegression()
    modelo.fit(X, y)

    # Datos nuevos del residuo
    nuevo = np.array([[residuo.get("peso_inicial_g", 0),
                       residuo.get("eficiencia_ajustada", 0),
                       residuo.get("tiempo_estimado_dias", 0)]])

    prediccion = modelo.predict(nuevo)[0]

    return {
        "prediccion_porcentaje_degradacion": round(prediccion, 2),
        "coeficientes": dict(zip(["peso_inicial_g", "eficiencia_ajustada", "tiempo_estimado_dias"], modelo.coef_)),
        "intercepto": modelo.intercept_
    }
