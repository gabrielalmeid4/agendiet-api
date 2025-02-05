from pydantic import BaseModel
import datetime

class Nutricionista(BaseModel):
    latitude: str
    longitude: str

    class Config:
        orm_mode = True