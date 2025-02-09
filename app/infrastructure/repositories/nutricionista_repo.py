import asyncpg
from typing import Optional, List

from fastapi import Depends
from app.domain.models.nutricionista import Nutricionista
from app.domain.repositories.base_nutricionista_repo import BaseNutricionistaRepository
from app.infrastructure.database.config import get_db

class NutricionistaRepository(BaseNutricionistaRepository):
    def __init__(self, db=Depends(get_db)):
        self.db = db
        
    async def salvar(self, nutricionista: Nutricionista):
        query = """
        INSERT INTO nutricionista (nome, latitude, longitude)
        VALUES ($1, $2, $3)
        """
        await self.db.execute(query, nutricionista.nome, nutricionista.latitude, nutricionista.longitude)

    async def get_all(self) -> List[Nutricionista]:
        query = "SELECT * FROM nutricionista"
        rows = await self.db.fetch(query)
        return rows

    async def get_by_id(self, id_nutricionista: int) -> Optional[Nutricionista]:
        query = "SELECT * FROM nutricionista WHERE id_nutricionista = $1"
        rows = await self.db.fetch(query, id_nutricionista)
        return rows

    async def remove(self, id_nutricionista: int):
        query = "DELETE FROM nutricionista WHERE id_nutricionista = $1"
        await self.db.execute(query, id_nutricionista)

    async def update(self, id_nutricionista: int, nutricionista: Nutricionista):
        query = """
        UPDATE nutricionista
        SET nome = $4, latitude = $2, longitude = $3
        WHERE id_nutricionista = $1
        """
        await self.db.execute(query, id_nutricionista, nutricionista.latitude, nutricionista.longitude, nutricionista.nome)
