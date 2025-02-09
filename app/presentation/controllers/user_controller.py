from fastapi import Depends, HTTPException
from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.infrastructure.repositories.user_repo import UserRepository
from app.domain.models.user import User
from app.domain.models.email_senha import EmailSenha
from app.infrastructure.database.config import get_db

SECRET_KEY = "chave_super_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class UserController:
    def __init__(self, user_repo: UserRepository = Depends(), db=Depends(get_db)):
        self.user_repo = user_repo

    async def registrar_usuario(self, user: User):
        await self.user_repo.salvar(user)
        return {"message": "Usuário registrado com sucesso!"}

    async def criar_token_acesso(self, data: dict, expires_delta: timedelta):
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    async def login(self, email_senha: EmailSenha):
        user = await self.user_repo.get_by_email_senha(email_senha.email, email_senha.senha)
        if not user:
            raise HTTPException(status_code=401, detail="Usuário ou senha inválidos.")
        
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = await self.criar_token_acesso(
            data={"sub": user["email"]}, expires_delta=access_token_expires
        )

        return {"access_token": access_token, "token_type": "bearer"}
