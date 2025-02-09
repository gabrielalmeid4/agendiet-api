from fastapi import Depends, HTTPException, Path
from app.infrastructure.repositories.meta_peso_repo import MetaPesoRepository
from app.domain.repositories.base_meta_peso_repo import BaseMetaPesoRepository
from app.infrastructure.database.config import get_db
from app.domain.models.meta_peso import MetaPeso

class MetaPesoController:
    def __init__(self, meta_peso_repo: BaseMetaPesoRepository = Depends(MetaPesoRepository), db=Depends(get_db)):
        self.meta_peso_repo = meta_peso_repo


    async def registrar_meta_peso(self, meta_peso: MetaPeso, id_usuario: int):
        await self.meta_peso_repo.salvar(meta_peso, id_usuario)
        return {"message": "Meta de Peso registrada com sucesso!"}

    async def get_metas_peso(self, id_usuario: int):
        metas_peso = await self.meta_peso_repo.get_by_id(id_usuario)
        if not metas_peso:
            raise HTTPException(status_code=200, detail="Metas de Peso não encontradas para este usuário.")
        return metas_peso

    async def delete_meta_peso(self, id_meta_peso: int):
        await self.meta_peso_repo.remove(id_meta_peso)
        return {"message": "Meta de Peso excluída com sucesso!"}

    async def update_meta_peso(self, meta_peso: MetaPeso, id_meta_peso: int):
        await self.meta_peso_repo.update(meta_peso, id_meta_peso)
        return {"message": "Meta de Peso atualizada com sucesso!"}
