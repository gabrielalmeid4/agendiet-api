from pydantic import BaseModel
import datetime
from typing import Optional

class PlanoAlimentar(BaseModel):
    nome: str
    tag: str
    horario_refeicao: str  
    descricao: str

    class Config:
        orm_mode = True
