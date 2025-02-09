import asyncpg
from typing import Optional, List, Any

from fastapi import Depends
from app.domain.models.user import User
from app.domain.repositories.base_user_repo import BaseUserRepository
from app.infrastructure.database.config import get_db
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserRepository(BaseUserRepository):
    def __init__(self, db=Depends(get_db)):
        self.db = db

    async def salvar(self, user: User):
        hashed_password = pwd_context.hash(user.password)  # Hash da password antes de salvar
        await self.db.execute(
            "INSERT INTO users (name, email, password, eh_nutricionista) VALUES ($1, $2, $3, $4)",
            user.name, user.email, hashed_password, user.eh_nutricionista
        )
        
    async def get_all(self) -> List[User]:
        query = "SELECT * FROM users"
        rows = await self.db.fetch(query)
        return [dict(row) for row in rows]
    
    async def get_by_id(self, id: str) -> Optional[User]:
        query = "SELECT * FROM users WHERE id = $1"
        row = await self.db.fetchrow(query, id)
        return dict(row) if row else None
    
    
    async def get_by_email(self, email: str):
        user = await self.db.fetchrow("SELECT * FROM users WHERE email = $1", email)
        return user

    async def verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    async def get_by_email_senha(self, email: str, password: str):
        user = await self.get_by_email(email)
        if user and await self.verify_password(password, user["password"]):
            return user
        return None
    
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
    
    
    
    