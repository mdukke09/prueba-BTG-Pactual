from pydantic import BaseModel
from typing import Optional

class TransactionCreate(BaseModel):
    user_id: str
    fund_id: str
    type: str
    amount: Optional[float] = None

class TransactionResponse(BaseModel):
    id: str
    user_id: str
    fund_id: str
    type: str
    amount: Optional[float] = None
    date: str
