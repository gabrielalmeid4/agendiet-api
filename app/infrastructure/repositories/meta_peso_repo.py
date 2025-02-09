import asyncpg
from typing import Optional, List, Any

from fastapi import Depends
from app.domain.models.meta_peso import MetaPeso
from app.domain.repositories.base_meta_peso_repo import BaseMetaPesoRepository
from app.infrastructure.database.config import get_db

class MetaPesoRepository(BaseMetaPesoRepository):
    def __init__(self, db=Depends(get_db)):
        self.db = db
        
    async def salvar(self, meta_peso: MetaPeso, id_usuario: int):
        query = """
        INSERT INTO meta_peso (id_usuario, peso_pretendido, data_inicio, data_limite, foi_atingido)
        VALUES ($1, $2, $3, $4, $5)
        """
        await self.db.execute(query, id_usuario, meta_peso.peso_pretendido,
                              meta_peso.data_inicio, meta_peso.data_limite, meta_peso.foi_atingido)

    async def get_all(self) -> List[MetaPeso]:
        query = "SELECT * FROM meta_peso"
        rows = await self.db.fetch(query)
        return rows

    async def get_by_id(self, id_usuario: int) -> Optional[MetaPeso]:
        query = "SELECT * FROM meta_peso WHERE id_usuario = $1"
        rows= await self.db.fetch(query, id_usuario)
        return rows
    
    async def remove(self, id: str):
        query = "DELETE FROM meta_peso WHERE id = $1"
        await self.db.execute(query, id)

    async def update(self, meta_peso: MetaPeso, id_meta: int):
        query = """
        UPDATE meta_peso
        SET peso_pretendido = $1, data_inicio = $2,
            data_limite = $3, foi_atingido = $4
        WHERE id = $5
        """
        await self.db.execute(query, meta_peso.peso_pretendido,
                              meta_peso.data_inicio, meta_peso.data_limite, meta_peso.foi_atingido, id_meta)