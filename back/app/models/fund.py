from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class Fund(BaseModel):
    _id: Optional[ObjectId]
    id: str
    name: str
    minimum_amount: float
    category: str