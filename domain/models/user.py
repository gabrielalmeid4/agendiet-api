from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str
    eh_nutricionista: bool

    class Config:
        orm_mode = True