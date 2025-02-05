from pydantic import BaseModel
import datetime

class Medicacao(BaseModel):
    nome: str
    dosagem_unica: bool
    intervalo: str
    data_inicio: str
    data_fim: str
    horario_inicio: str

    class Config:
        orm_mode = True