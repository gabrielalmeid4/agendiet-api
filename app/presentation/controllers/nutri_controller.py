from fastapi import Depends, HTTPException, Path
from app.infrastructure.repositories.nutricionista_repo import NutricionistaRepository
from app.domain.repositories.base_nutricionista_repo import BaseNutricionistaRepository
from app.infrastructure.database.config import get_db
from app.domain.models.nutricionista import Nutricionista

class NutricionistaController:
    def __init__(self, nutri_repo: BaseNutricionistaRepository = Depends(NutricionistaRepository), db=Depends(get_db)):
        self.nutri_repo = nutri_repo

    async def registrar_nutricionista(self, nutricionista: Nutricionista):
        id_nutricionista = await self.nutri_repo.salvar(nutricionista)
        return {"message": "Nutricionista registrado com sucesso!", "id_nutricionista": id_nutricionista}

    async def get_nutricionistas(self):
        nutricionistas = await self.nutri_repo.get_all()
        if not nutricionistas:
            raise HTTPException(status_code=404, detail="Nenhum nutricionista encontrado.")
        return nutricionistas

    async def get_nutricionista(self, id_nutricionista: int):
        nutricionista = await self.nutri_repo.get_by_id(id_nutricionista)
        if not nutricionista:
            raise HTTPException(status_code=404, detail="Nutricionista não encontrado.")
        return nutricionista

    async def delete_nutricionista(self, id_nutricionista: int):
        deletado = await self.nutri_repo.delete(id_nutricionista)
        if not deletado:
            raise HTTPException(status_code=404, detail="Nutricionista não encontrado para exclusão.")
        return {"message": "Nutricionista excluído com sucesso!"}
