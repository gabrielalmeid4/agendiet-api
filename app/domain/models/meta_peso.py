from pydantic import BaseModel
import datetime

class MetaPeso(BaseModel):
    peso_pretendido: float
    data_inicio: str
    data_limite: str
    foi_atingido: bool

    class Config:
        orm_mode = True
