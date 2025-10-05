import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
from app.models.simulacion_model import listar_simulaciones

# Entrenador IA BioAI
async def entrenar_modelo_bioai():
    """
    Entrena un modelo de regresión lineal para predecir el porcentaje de degradación.
    Basado en las simulaciones previas de MongoDB.
    """
    simulaciones = await listar_simulaciones()
    if not simulaciones:
        return {"message": "No hay datos suficientes para entrenar el modelo."}

    # Crear dataset a partir de las simulaciones
    df = pd.DataFrame(simulaciones)

    # Verificar columnas necesarias
    columnas_requeridas = [
        "porcentaje_degradacion", "peso_inicial_g",
        "eficiencia_ajustada", "tiempo_estimado_dias"
    ]
    for col in columnas_requeridas:
        if col not in df.columns:
            return {"message": f"Falta columna {col} en los datos para entrenar el modelo."}

    # Variables de entrada (X) y salida (y)
    X = df[["peso_inicial_g", "eficiencia_ajustada", "tiempo_estimado_dias"]]
    y = df["porcentaje_degradacion"]

    # División entrenamiento / prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Modelo de regresión lineal
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    # Predicciones
    y_pred = modelo.predict(X_test)

    # Métricas de evaluación
    r2 = round(r2_score(y_test, y_pred), 3)
    mae = round(mean_absolute_error(y_test, y_pred), 3)

    # Coeficientes del modelo
    coeficientes = dict(zip(X.columns, modelo.coef_))

    return {
        "message": "Modelo entrenado exitosamente",
        "r2_score": r2,
        "mean_absolute_error": mae,
        "coeficientes": coeficientes,
        "intercepto": modelo.intercept_
    }
