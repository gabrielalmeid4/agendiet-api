import asyncpg
from typing import Optional, List, Any
from domain.models.peso import Peso
from domain.repositories.base_repo import BaseRepository

class PesoRepository(BaseRepository):
    async def salvar(self, peso: Peso, id_usuario: int):
        query = """
        INSERT INTO peso (id_usuario, peso, data)
        VALUES ($1, $2, $3)
        """
        await self.db.execute(query, id_usuario, peso.peso, peso.data)

    async def get_all(self) -> List[Peso]:
        query = "SELECT * FROM peso"
        rows = await self.db.fetch(query)
        return rows

    async def get_by_id(self, id: int) -> Optional[Peso]:
        query = "SELECT * FROM peso WHERE id_usuario = $1"
        row = await self.db.fetch(query, id)
        return row

    async def remove(self, id: int):
        query = "DELETE FROM peso WHERE id = $1"
        await self.db.execute(query, id)

    async def update(self, peso: Peso, id_peso: int):
        query = """
        UPDATE peso 
        SET peso = $1, data = $2
        WHERE id = $3
        """
        await self.db.execute(query, peso.peso, peso.data, id_peso)

    async def get_latest(self, id_usuario: int) -> Optional[Peso]:
        query = """
        SELECT * FROM peso 
        WHERE id_usuario = $1 
        ORDER BY data DESC 
        LIMIT 1
        """
        row = await self.db.fetchrow(query, id_usuario)
        return row