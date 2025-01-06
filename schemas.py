from pydantic import BaseModel
from typing import Dict

class DIDCreate(BaseModel):
    did: str
    controller: str
    document: Dict  # Asegúrate de que sea un diccionario

class DIDResponse(DIDCreate):
    id: int

    class Config:
        orm_mode = True
