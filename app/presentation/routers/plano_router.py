from fastapi import APIRouter, Depends
from app.presentation.controllers.plano_controller import PlanoController
from app.domain.models.plano_alimentar import PlanoAlimentar

router = APIRouter(prefix="/planos-alimentares", tags=["Planos Alimentares"])

plano_controller = PlanoController()

@router.post("/registrar/{id_usuario}")
async def registrar_plano(plano_alimentar: PlanoAlimentar, id_usuario: int, plano_controller: PlanoController = Depends()):
    return await plano_controller.registrar_plano(plano_alimentar, id_usuario)

@router.get("/get/{id_usuario}/{dia}")
async def get_planos(id_usuario: int, dia: str, plano_controller: PlanoController = Depends()):
    return await plano_controller.get_planos_alimentares(id_usuario, dia)

@router.delete("/delete/{id_plano_alimentar}")
async def delete_plano(id_plano_alimentar: int, plano_controller: PlanoController = Depends()):
    return await plano_controller.delete_plano(id_plano_alimentar)

@router.put("/update/{id_plano_alimentar}")
async def update_plano(plano_alimentar: PlanoAlimentar, id_plano_alimentar: int, plano_controller: PlanoController = Depends()):
    return await plano_controller.update_plano(plano_alimentar, id_plano_alimentar)
