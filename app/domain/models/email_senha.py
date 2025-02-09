from pydantic import BaseModel
import datetime

class EmailSenha(BaseModel):
    email: str
    senha: str

    class Config:
        orm_mode = True