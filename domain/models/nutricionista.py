from pydantic import BaseModel
import datetime

class Nutricionista(BaseModel):
    nome: str
    latitude: str
    longitude: str

    class Config:
        orm_mode = True
