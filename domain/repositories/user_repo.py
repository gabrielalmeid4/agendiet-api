import asyncpg
from typing import Optional, List, Any
from domain.models.user import User
from domain.repositories.base_repo import BaseRepository

class UserRepository(BaseRepository):
    async def salvar(self, user: User):
        query = """
        INSERT INTO users (name, email, password, eh_nutricionista)
        VALUES ($1, $2, $3, $4)
        """
        await self.db.execute(query, user.name, user.email, user.password, user.eh_nutricionista)

    async def get_all(self) -> List[User]:
        query = "SELECT * FROM users"
        rows = await self.db.fetch(query)
        return [dict(row) for row in rows]

    async def get_by_id(self, id: str) -> Optional[User]:
        query = "SELECT * FROM users WHERE id = $1"
        row = await self.db.fetchrow(query, id)
        return dict(row) if row else None
    
    async def get_by_email_senha(self, email: str, senha: str) -> Optional[User]:
        query = "SELECT id FROM users WHERE email = $1 AND password = $2"
        row = await self.db.fetchrow(query, email, senha)
        return dict(row) if row else None

    async def remove(self, id: str):
        query = "DELETE FROM users WHERE id = $1"
        await self.db.execute(query, id)
    
    async def update(self, user: User, id_usuario: int):
        query = """
        UPDATE users
        SET name = $2, email = $3, password = $4, eh_nutricionista = $5
        WHERE id = $1
        """
        await self.db.execute(query, id_usuario, user.name, user.email, user.password, user.eh_nutricionista)