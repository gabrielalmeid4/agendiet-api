from fastapi import Depends, HTTPException, Path
from app.infrastructure.repositories.plano_alimentar_repo import PlanoAlimentarRepository
from app.domain.repositories.base_plano_repo import BasePlanoAlimentarRepository
from app.infrastructure.database.config import get_db
from app.domain.models.plano_alimentar import PlanoAlimentar

class PlanoController:
    def __init__(self, plano_repo: BasePlanoAlimentarRepository = Depends(PlanoAlimentarRepository), db=Depends(get_db)):
        self.plano_repo = plano_repo

    async def registrar_plano(self, plano_alimentar: PlanoAlimentar, id_usuario: int):
        await self.plano_repo.salvar(plano_alimentar, id_usuario)
        return {"message": "Plano Alimentar registrado com sucesso!"}

    async def get_planos_alimentares(self, id_usuario: int, dia: str):
        planos_alimentares = await self.plano_repo.get_by_id(id_usuario, dia)
        if not planos_alimentares:
            raise HTTPException(status_code=404, detail="Plano Alimentar não encontrado para este usuário.")
        return planos_alimentares

    async def delete_plano(self, id_plano_alimentar: int):
        await self.plano_repo.remove(id_plano_alimentar)
        return {"message": "Plano Alimentar excluído com sucesso!"}

    async def update_plano(self, plano_alimentar: PlanoAlimentar, id_plano_alimentar: int):
        await self.plano_repo.update(plano_alimentar, id_plano_alimentar)
        return {"message": "Plano Alimentar atualizado com sucesso!"}
