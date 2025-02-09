from fastapi import APIRouter, Depends, Path
from app.presentation.controllers.peso_controller import PesoController
from app.domain.models.peso import Peso

router = APIRouter(prefix="/pesos", tags=["Pesos"])

peso_controller = PesoController()

@router.post("/registrar/{id_usuario}")
async def registrar_peso(peso: Peso, id_usuario: int = Path(..., title="ID do Usuário"), peso_controller: PesoController = Depends()):
    return await peso_controller.registrar_peso(peso, id_usuario)

@router.get("/get/{id_usuario}")
async def get_pesos(id_usuario: int = Path(..., title="ID do Usuário"), peso_controller: PesoController = Depends()):
    return await peso_controller.get_pesos(id_usuario)

@router.delete("/delete/{id_peso}")
async def delete_peso(id_peso: int = Path(..., title="ID do Peso"), peso_controller: PesoController = Depends()):
    return await peso_controller.delete_peso(id_peso)

@router.get("/latest/{id_usuario}")
async def get_latest_peso(id_usuario: int = Path(..., title="ID do Usuário"), peso_controller: PesoController = Depends()):
    return await peso_controller.get_latest_peso(id_usuario)

@router.put("/update/{id_peso}")
async def update_peso(peso: Peso, id_peso: int = Path(..., title="ID do Peso"), peso_controller: PesoController = Depends()):
    return await peso_controller.update_peso(peso, id_peso)
