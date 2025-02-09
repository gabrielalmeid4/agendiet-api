from fastapi import Depends, HTTPException
from app.infrastructure.repositories.user_repo import UserRepository
from app.domain.repositories.base_user_repo import BaseUserRepository
from app.infrastructure.database.config import get_db
from app.domain.models.user import User
from app.domain.models.email_senha import EmailSenha

class UserController:
    def __init__(self, user_repo: BaseUserRepository = Depends(UserRepository), db=Depends(get_db)):
        self.user_repo = user_repo

    async def registrar_usuario(self, user: User):
        await self.user_repo.salvar(user)
        return {"message": "Usuário registrado com sucesso!"}

    async def login(self, email_senha: EmailSenha):
        user = await self.user_repo.get_by_email_senha(email_senha.email, email_senha.senha)
        if not user:
            raise HTTPException(status_code=401, detail="Usuário ou senha inválidos.")
        return {"id": user["id"], "name": user["name"]}
