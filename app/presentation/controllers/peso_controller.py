from fastapi import Depends, HTTPException, Path
from app.infrastructure.repositories.peso_repo import PesoRepository
from app.domain.repositories.base_peso_repo import BasePesoRepository
from app.infrastructure.database.config import get_db
from app.domain.models.peso import Peso

class PesoController:
    def __init__(self, peso_repo: BasePesoRepository = Depends(PesoRepository), db=Depends(get_db)):
        self.peso_repo = peso_repo

    async def registrar_peso(self, peso: Peso, id_usuario: int):
        await self.peso_repo.salvar(peso, id_usuario)
        return {"message": "Peso registrado com sucesso!"}

    async def get_pesos(self, id_usuario: int):
        pesos = await self.peso_repo.get_by_id(id_usuario)
        if not pesos:
            raise HTTPException(status_code=200, detail="Pesos não encontrados para este usuário.")
        return pesos

    async def delete_peso(self, id_peso: int):
        await self.peso_repo.remove(id_peso)
        return {"message": "Peso excluído com sucesso!"}

    async def get_latest_peso(self, id_usuario: int):
        latest_peso = await self.peso_repo.get_latest(id_usuario)
        if not latest_peso:
            raise HTTPException(status_code=404, detail="Nenhum peso registrado para este usuário.")
        return latest_peso

    async def update_peso(self, peso: Peso, id_peso: int):
        await self.peso_repo.update(peso, id_peso)
        return {"message": "Peso atualizado com sucesso!"}
