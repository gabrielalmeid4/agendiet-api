import asyncpg
from typing import Optional, List, Any

from fastapi import Depends
from app.domain.models.plano_alimentar import PlanoAlimentar
from app.domain.repositories.base_plano_repo import BasePlanoAlimentarRepository
from app.infrastructure.database.config import get_db

class PlanoAlimentarRepository(BasePlanoAlimentarRepository):
    def __init__(self, db=Depends(get_db)):
        self.db = db
        
    async def salvar(self, plano_alimentar: PlanoAlimentar, id_usuario: int):
        query = """
        INSERT INTO plano_alimentar (nome, id_usuario, id_nutricionista, tag, descricao, horario, dia)
        VALUES ($1, $2, $3, $4, $5, $6, $7)
        """
        await self.db.execute(query, plano_alimentar.nome, id_usuario, 
                              None, plano_alimentar.tag, 
                              plano_alimentar.descricao, plano_alimentar.horario, plano_alimentar.dia)


    async def get_all(self) -> List[PlanoAlimentar]:
        query = "SELECT * FROM plano_alimentar"
        rows = await self.db.fetch(query)
        return rows

    async def get_by_id(self, id_usuario: int, dia: str) -> Optional[PlanoAlimentar]:
        query = "SELECT * FROM plano_alimentar WHERE id_usuario = $1 AND dia = $2"
        rows= await self.db.fetch(query, id_usuario, dia)
        return rows

    async def remove(self, id: str):
        query = "DELETE FROM plano_alimentar WHERE id = $1"
        await self.db.execute(query, id)
        
    async def update(self, plano_alimentar: PlanoAlimentar, id_plano: int):
        query = """
        UPDATE plano_alimentar
        SET nome = $1, tag = $2, descricao = $3, horario = $4, dia = $5
        WHERE id = $6
        """
        await self.db.execute(query, plano_alimentar.nome, plano_alimentar.tag,
                              plano_alimentar.descricao, plano_alimentar.horario, plano_alimentar.dia, id_plano)