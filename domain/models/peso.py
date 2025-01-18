from pydantic import BaseModel

class Peso(BaseModel):
    peso: float
    data: str 

    class Config:
        orm_mode = True

