from fastapi import APIRouter, HTTPException
from app.schemas.usuario_schema import UsuarioSchema
from app.models.usuario_model import crear_usuario, listar_usuarios

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=dict)
async def crear_usuario_endpoint(usuario: UsuarioSchema):
    try:
        data = usuario.dict(by_alias=True)
        nuevo_usuario = await crear_usuario(data)
        return {"message": "Usuario creado exitosamente", "data": nuevo_usuario}
    except Exception as e:
        print("Error en endpoint /usuarios:", e)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=dict)
async def listar_usuarios_endpoint():
    try:
        usuarios = await listar_usuarios()
        return {"usuarios": usuarios}
    except Exception as e:
        print("Error al listar usuarios:", e)
        raise HTTPException(status_code=500, detail=str(e))
