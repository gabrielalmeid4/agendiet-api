from config import get_db
from fastapi import APIRouter, HTTPException, Depends, Path

from domain.models.medicacao import Medicacao
from domain.models.meta_peso import MetaPeso
from domain.models.user import User
from domain.models.peso import Peso
from domain.models.plano_alimentar import PlanoAlimentar

from domain.repositories.medicacao_repo import MedicacaoRepository
from domain.repositories.meta_peso_repo import MetaPesoRepository
from domain.repositories.peso_repo import PesoRepository
from domain.repositories.plano_alimentar_repo import PlanoAlimentarRepository
from domain.repositories.user_repo import UserRepository
from domain.models.email_senha import EmailSenha

router = APIRouter()


#Usuarios
@router.post("/registrar-usuario")
async def registrar_usuario(user: User, db = Depends(get_db)):
    user_repo = UserRepository(db)

    await user_repo.salvar(user)

    return {"message": "Usuário registrado com sucesso!"}

@router.get("/login")
async def login(email_senha: EmailSenha, db = Depends(get_db)):
     user_repo = UserRepository(db)
     email = email_senha.email
     senha = email_senha.senha
     print(email, senha)
     user = await user_repo.get_by_email_senha(email, senha)
     
     if not user:
         raise HTTPException(status_code=401, detail="Usuário ou senha inválidos.")
     
     return {"message": "Login realizado com sucesso!"}
 
#Meta Peso
@router.get("/metas-peso/registrar/{id_usuario}")
async def registrar_meta_peso(meta_peso: MetaPeso, id_usuario: int = Path(..., title="ID do Usuário"),  db = Depends(get_db)):
     meta_peso_repo = MetaPesoRepository(db)
     await meta_peso_repo.salvar(meta_peso, id_usuario)
     
     return {"message": "Meta de Peso registrada com sucesso!"}

@router.get("/metas-peso/get/{id_usuario}")
async def get_metas_peso(id_usuario: int = Path(..., title="ID do Usuário"), db = Depends(get_db)):
     meta_peso_repo = MetaPesoRepository(db)
     metas_peso = await meta_peso_repo.get_by_id(id_usuario)
     
     if not metas_peso:
         raise HTTPException(status_code=404, detail="Metas de Peso não encontradas para este usuário.")
     
     return metas_peso
 
@router.post("/metas-peso/delete/{id_meta_peso}")
async def delete_meta_peso(id_meta_peso: int = Path(..., title="ID da Meta de Peso"), db = Depends(get_db)):
     plano_alimentar_repo = PlanoAlimentarRepository(db)
     await plano_alimentar_repo.remove(id_meta_peso)
     
     return {"message": "Meta de Peso excluída com sucesso!"}
 
@router.post("/metas-peso/update/{id_meta_peso}")
async def update_meta_peso(meta_peso: MetaPeso, id_meta_peso: int = Path(..., title="ID da Meta de Peso"),  db = Depends(get_db)):
     plano_alimentar_repo = PlanoAlimentarRepository(db)
     await plano_alimentar_repo.update(id_meta_peso, meta_peso)
     
     return {"message": "Meta de Peso atualizada com sucesso!"}
 
#Plano Alimentar
@router.post("/planos-alimentares/registrar/{id_usuario}")
async def registrar_plano(plano_alimentar: PlanoAlimentar, id_usuario: int = Path(..., title="ID do Usuário"), db = Depends(get_db)):
     plano_alimentar_repo = PlanoAlimentarRepository(db)
     await plano_alimentar_repo.salvar(plano_alimentar, id_usuario)
     
     return {"message": "Plano Alimentar registrado com sucesso!"}
 
@router.get("/planos-alimentares/get/{id_usuario}")
async def get_planos_alimentares(id_usuario: int = Path(..., title="ID do Usuário"), db = Depends(get_db)):
     plano_alimentar_repo = PlanoAlimentarRepository(db)
     planos_alimentares = await plano_alimentar_repo.get_by_id(id_usuario)
     
     if not planos_alimentares:
         raise HTTPException(status_code=404, detail="Plano Alimentar não encontrado para este usuário.")
     
     return planos_alimentares

@router.post("/planos-alimentares/delete/{id_plano_alimentar}")
async def delete_plano(id_plano_alimentar: int = Path(..., title="ID do Plano Alimentar"), db = Depends(get_db)):
     plano_alimentar_repo = PlanoAlimentarRepository(db)
     await plano_alimentar_repo.remove(id_plano_alimentar)
     
     return {"message": "Plano Alimentar excluído com sucesso!"}
 
@router.post("/planos-alimentares/update/{id_plano_alimentar}")
async def update_plano(plano_alimentar: PlanoAlimentar, id_plano_alimentar: int = Path(..., title="ID do Plano Alimentar"),  db = Depends(get_db)):
     plano_alimentar_repo = PlanoAlimentarRepository(db)
     await plano_alimentar_repo.update(id_plano_alimentar, plano_alimentar)
     
     return {"message": "Plano Alimentar atualizado com sucesso!"}

#Medicacoes
@router.post("/medicacoes/registrar/{id_usuario}")
async def registrar_medicacao(medicacao: Medicacao, id_usuario: int = Path(..., title="ID do Usuário"), db = Depends(get_db)):
     medicacao_repo = MedicacaoRepository(db)
     await medicacao_repo.salvar(medicacao, id_usuario)
     
     return {"message": "Medicação registrada com sucesso!"}

@router.get("/medicacoes/get/{id_usuario}")
async def get_medicacoes(id_usuario: int = Path(..., title="ID do Usuário"), db = Depends(get_db)):
     medicacao_repo = MedicacaoRepository(db)
     medicacoes = await medicacao_repo.get_by_id(id_usuario)
     
     if not medicacoes:
         raise HTTPException(status_code=404, detail="Medicações não encontradas para este usuário.")
     
     return medicacoes

@router.post("/medicacoes/delete/{id_medicacao}")
async def delete_medicacao(id_medicacao: int = Path(..., title="ID da Medicação"), db = Depends(get_db)):
     medicacao_repo = MedicacaoRepository(db)
     await medicacao_repo.remove(id_medicacao)
     
     return {"message": "Medicação excluída com sucesso!"}
 
@router.post("/medicacoes/update/{id_medicacao}")
async def update_medicacao(medicacao: Medicacao, id_medicacao: int = Path(..., title="ID da Medicação"),  db = Depends(get_db)):  
     medicacao_repo = MedicacaoRepository(db)
     await medicacao_repo.update(id_medicacao, medicacao)
     
     return {"message": "Medicação atualizada com sucesso!"}
 
