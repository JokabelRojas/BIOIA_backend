from fastapi import FastAPI
from app.routes.usuario_routes import router as usuario_router
from app.routes.residuo_routes import router as residuo_router 
from app.routes.simulacion_routes import router as simulacion_router
from app.routes.bacteria_routes import router as bacteria_router
from app.routes.entorno_routes import router as entorno_router
from app.routes.recomendacion_routes import router as recomendacion_router
from app.routes.ia_routes import router as ia_router
from app.routes.ia_predict_routes import router as ia_predict_router
from app.routes.resultado_routes import router as resultado_router
from app.routes.dashboard_routes import router as dashboard_router
from app.routes.export_routes import router as export_router

app = FastAPI(
    title="BioAI Backend",
    description="Simulación Inteligente de Gestión de Residuos Sólidos",
    version="1.0"
)

app.include_router(usuario_router)
app.include_router(residuo_router)
app.include_router(simulacion_router)
app.include_router(bacteria_router)
app.include_router(entorno_router)
app.include_router(recomendacion_router)
app.include_router(ia_router)
app.include_router(ia_predict_router)
app.include_router(resultado_router)
app.include_router(dashboard_router)
app.include_router(export_router)


@app.get("/")
async def root():
    return {
        "message": "Bienvenida al backend de BioAI - Gestión Inteligente de Residuos"
    }
