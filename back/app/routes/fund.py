from fastapi import APIRouter, HTTPException
from app.schemas.fund import FundResponse
from app.database import get_fund_collection
from typing import List

router = APIRouter()

@router.get("/funds", response_model=List[FundResponse])
async def get_funds():
    fund_collection = get_fund_collection()
    funds = await fund_collection.find().to_list(100)
    for fund in funds:
        fund["id"] = str(fund["id"])
    return funds

@router.get("/funds/{fund_id}", response_model=FundResponse)
async def get_fund(fund_id: str):
    fund_collection = get_fund_collection()
    fund = await fund_collection.find_one({"id": fund_id})
    if not fund:
        raise HTTPException(status_code=404, detail="Fondo no encontrado")
    fund["id"] = str(fund["id"])
    return fund