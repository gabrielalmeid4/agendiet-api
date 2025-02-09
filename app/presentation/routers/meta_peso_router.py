from fastapi import APIRouter, Depends, Path
from app.presentation.controllers.meta_peso_controller import MetaPesoController
from app.domain.models.meta_peso import MetaPeso

router = APIRouter(prefix="/metas-peso", tags=["Metas de Peso"])

meta_peso_controller = MetaPesoController()

@router.post("/registrar/{id_usuario}")
async def registrar_meta_peso(meta_peso: MetaPeso, id_usuario: int = Path(..., title="ID do Usuário"), meta_peso_controller: MetaPesoController = Depends()):
    return await meta_peso_controller.registrar_meta_peso(meta_peso, id_usuario)

@router.get("/get/{id_usuario}")
async def get_metas_peso(id_usuario: int = Path(..., title="ID do Usuário"), meta_peso_controller: MetaPesoController = Depends()):
    return await meta_peso_controller.get_metas_peso(id_usuario)

@router.delete("/delete/{id_meta_peso}")
async def delete_meta_peso(id_meta_peso: int = Path(..., title="ID da Meta de Peso"), meta_peso_controller: MetaPesoController = Depends()):
    return await meta_peso_controller.delete_meta_peso(id_meta_peso)

@router.put("/update/{id_meta_peso}")
async def update_meta_peso(meta_peso: MetaPeso, id_meta_peso: int = Path(..., title="ID da Meta de Peso"), meta_peso_controller: MetaPesoController = Depends()):
    return await meta_peso_controller.update_meta_peso(meta_peso, id_meta_peso)
