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
        hashed_password = pwd_context.hash(user.senha)  # Hash da senha antes de salvar
        await self.db.execute(
            "INSERT INTO users (name, email, senha) VALUES ($1, $2, $3)",
            user.name, user.email, hashed_password
        )

    async def get_by_email(self, email: str):
        user = await self.db.fetchrow("SELECT * FROM users WHERE email = $1", email)
        return user

    async def verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    async def get_by_email_senha(self, email: str, senha: str):
        user = await self.get_by_email(email)
        if user and await self.verify_password(senha, user["senha"]):
            return user
        return None