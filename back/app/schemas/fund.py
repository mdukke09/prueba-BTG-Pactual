from pydantic import BaseModel

class FundBase(BaseModel):
    id: str
    name: str
    minimum_amount: float
    category: str

class FundCreate(FundBase):
    pass

class FundResponse(FundBase):
    id: str
