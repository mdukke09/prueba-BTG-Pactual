from fastapi import APIRouter, HTTPException
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.database import get_transaction_collection, get_user_collection, get_fund_collection
from bson import ObjectId
from datetime import datetime, timezone
from typing import List

router = APIRouter()

@router.post("/transactions", response_model=TransactionResponse)
async def create_transaction(transaction: TransactionCreate):
    user_collection = get_user_collection()
    fund_collection = get_fund_collection()
    transaction_collection = get_transaction_collection()

    user = await user_collection.find_one({"id": transaction.user_id})
    fund = await fund_collection.find_one({"id": transaction.fund_id})

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    if not fund:
        raise HTTPException(status_code=404, detail="Fondo no encontrado")

    if transaction.type == "subscription":
        if transaction.amount < fund["minimum_amount"]:
            raise HTTPException(status_code=400, detail=f"El monto de la suscripción debe ser al menos {fund['minimum_amount']}")
        if user["balance"] < transaction.amount:
            raise HTTPException(status_code=400, detail=f"No tiene saldo disponible para vincularse al fondo {fund['name']}")
        user["balance"] -= transaction.amount
        await user_collection.update_one({"id": transaction.user_id}, {"$set": {"balance": user["balance"]}})
    elif transaction.type == "cancellation":
        recent_subscription = await transaction_collection.find_one(
            {"user_id": transaction.user_id, "fund_id": transaction.fund_id, "type": "subscription"},
            sort=[("date", -1)]
        )
        if not recent_subscription:
            raise HTTPException(status_code=404, detail="No se encontró una suscripción previa para cancelar")
        
        transaction.amount = recent_subscription["amount"]
        user["balance"] += transaction.amount
        await user_collection.update_one({"id": transaction.user_id}, {"$set": {"balance": user["balance"]}})

    transaction_dict = transaction.model_dump()
    transaction_dict["date"] = datetime.now(timezone.utc)
    new_transaction = await transaction_collection.insert_one(transaction_dict)
    created_transaction = await transaction_collection.find_one({"_id": new_transaction.inserted_id})

    created_transaction["id"] = str(created_transaction["_id"])
    created_transaction["date"] = created_transaction["date"].isoformat()

    return created_transaction


@router.get("/transactions", response_model=List[TransactionResponse])
async def get_transactions():
    transaction_collection = get_transaction_collection()
    transactions = await transaction_collection.find().to_list(100)

    for transaction in transactions:
        transaction["id"] = str(transaction["_id"])
        transaction["date"] = transaction["date"].isoformat()

    return transactions