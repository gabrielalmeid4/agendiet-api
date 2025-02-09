from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.presentation.controllers.user_controller import UserController
from app.domain.models.user import User
from app.domain.models.email_senha import EmailSenha
from jose import JWTError, jwt

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "chave_super_secreta"
ALGORITHM = "HS256"

user_controller = UserController()

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return {"email": email}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

@router.post("/registrar-usuario")
async def registrar_usuario(user: User, controller: UserController = Depends()):
    return await controller.registrar_usuario(user)

@router.post("/login")
async def login(email_senha: EmailSenha, controller: UserController = Depends()):
    return await controller.login(email_senha)

@router.get("/perfil")
async def perfil(current_user: dict = Depends(get_current_user)):
    return {"message": f"Perfil do usuário {current_user['email']}"}
