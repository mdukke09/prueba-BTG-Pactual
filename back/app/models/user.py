from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId

class User(BaseModel):
    _id: Optional[ObjectId]
    id: str
    name: str
    email: str
    phone: str
    balance: float
    funds: List[dict]

    class Config:
        arbitrary_types_allowed = True