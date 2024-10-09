from pydantic import BaseModel

class TransactionCreate(BaseModel):
    user_id: str
    fund_id: str
    type: str
    amount: float

class TransactionResponse(BaseModel):
    id: str
    user_id: str
    fund_id: str
    type: str
    amount: float
    date: str