import asyncpg
from typing import Optional, List, Any
from domain.models.medicacao import Medicacao
from domain.repositories.base_repo import BaseRepository

class MedicacaoRepository(BaseRepository):
    async def salvar(self, medicacao: Medicacao, id_usuario: int):
        query = """
        INSERT INTO medicacao (id_usuario, nome, dosagem_unica, intervalo, data_inicio, data_fim, horario_inicio)
        VALUES ($1, $2, $3, $4, $5, $6, $7)
        """
        await self.db.execute(query, id_usuario, medicacao.nome,
                              medicacao.dosagem_unica, medicacao.intervalo, medicacao.data_inicio,
                              medicacao.data_fim, medicacao.horario_inicio)
        
    async def get_all(self) -> List[Medicacao]:
        query = "SELECT * FROM medicacao"
        rows = await self.db.fetch(query)
        return rows

    async def get_by_id(self, id_usuario: int) -> Optional[Medicacao]:
        query = "SELECT * FROM medicacao WHERE id_usuario = $1"
        rows= await self.db.fetch(query, id_usuario)
        return rows
    
    async def remove(self, id_medicacao: str):
        query = "DELETE FROM medicacao WHERE id_medicacao = $1"
        await self.db.execute(query, id_medicacao)
        
    async def update(self, medicacao: Medicacao, id_medicacao: int):
        query = """
        UPDATE medicacao
        SET nome = $2, dosagem_unica = $3, intervalo = $4,
            data_inicio = $5, data_fim = $6, horario_inicio = $7
        WHERE id_medicacao = $1
        """
        await self.db.execute(query, id_medicacao, medicacao.nome,
                              medicacao.dosagem_unica, medicacao.intervalo, medicacao.data_inicio,
                              medicacao.data_fim, medicacao.horario_inicio)