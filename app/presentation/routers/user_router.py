from fastapi import APIRouter, Depends
from app.presentation.controllers.user_controller import UserController
from app.domain.models.user import User
from app.domain.models.email_senha import EmailSenha

router = APIRouter()

user_controller = UserController()

@router.post("/registrar-usuario")
async def registrar_usuario(user: User, controller: UserController = Depends()):
    return await controller.registrar_usuario(user)

@router.post("/login")
async def login(email_senha: EmailSenha, controller: UserController = Depends()):
    return await controller.login(email_senha)
