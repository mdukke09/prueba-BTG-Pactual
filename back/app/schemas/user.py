from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    id: str
    name: str
    email: str
    phone: str

class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    phone: str
    balance: float
    funds: List[dict]