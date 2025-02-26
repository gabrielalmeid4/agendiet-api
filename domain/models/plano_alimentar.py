from pydantic import BaseModel
import datetime
from typing import Optional

class PlanoAlimentar(BaseModel):
    nome: str
    tag: str
    descricao: str
    horario: str
    dia: str

    class Config:
        orm_mode = True
