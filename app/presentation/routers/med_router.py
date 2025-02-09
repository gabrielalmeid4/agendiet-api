from fastapi import APIRouter, Depends
from app.presentation.controllers.med_controller import MedicacaoController
from app.domain.models.medicacao import Medicacao

router = APIRouter(prefix="/medicacoes", tags=["Medicações"])

@router.post("/registrar/{id_usuario}")
async def registrar_medicacao(medicacao: Medicacao, id_usuario: int, medicacao_controller: MedicacaoController = Depends()):
    return await medicacao_controller.registrar_medicacao(medicacao, id_usuario)

@router.get("/get/{id_usuario}")
async def get_medicacoes(id_usuario: int, medicacao_controller: MedicacaoController = Depends()):
    return await medicacao_controller.get_medicacoes(id_usuario)

@router.delete("/delete/{id_medicacao}")
async def delete_medicacao(id_medicacao: int, medicacao_controller: MedicacaoController = Depends()):
    return await medicacao_controller.delete_medicacao(id_medicacao)

@router.put("/update/{id_medicacao}")
async def update_medicacao(medicacao: Medicacao, id_medicacao: int, medicacao_controller: MedicacaoController = Depends()):
    return await medicacao_controller.update_medicacao(medicacao, id_medicacao)
