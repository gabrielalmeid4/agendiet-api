from fastapi import Depends, HTTPException, Path
from app.infrastructure.repositories.medicacao_repo import MedicacaoRepository
from app.domain.repositories.base_medicacao_repo import BaseMedicacaoRepository
from app.infrastructure.database.config import get_db
from app.domain.models.medicacao import Medicacao

class MedicacaoController:
    def __init__(self, medicacao_repo: BaseMedicacaoRepository = Depends(MedicacaoRepository), db=Depends(get_db)):
        self.medicacao_repo = medicacao_repo

    async def registrar_medicacao(self, medicacao: Medicacao, id_usuario: int):
        await self.medicacao_repo.salvar(medicacao, id_usuario)
        return {"message": "Medicação registrada com sucesso!"}

    async def get_medicacoes(self, id_usuario: int):
        medicacoes = await self.medicacao_repo.get_by_id(id_usuario)
        if not medicacoes:
            raise HTTPException(status_code=404, detail="Medicações não encontradas para este usuário.")
        return medicacoes

    async def delete_medicacao(self, id_medicacao: int):
        await self.medicacao_repo.remove(id_medicacao)
        return {"message": "Medicação excluída com sucesso!"}

    async def update_medicacao(self, medicacao: Medicacao, id_medicacao: int):
        await self.medicacao_repo.update(id_medicacao, medicacao)
        return {"message": "Medicação atualizada com sucesso!"}
