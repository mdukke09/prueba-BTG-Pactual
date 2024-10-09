from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb://localhost:27017"
# MONGO_DETAILS = "mongodb://host.docker.internal:27017"
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.btg_pactual
fund_collection = database.get_collection("funds")

FUNDS = [
    {"id": '1', "name": "FPV_BTG_PACTUAL_RECAUDADORA", "minimum_amount": 75000, "category": "FPV"},
    {"id": '2', "name": "FPV_BTG_PACTUAL_ECOPETROL", "minimum_amount": 125000, "category": "FPV"},
    {"id": '3', "name": "DEUDAPRIVADA", "minimum_amount": 50000, "category": "FIC"},
    {"id": '4', "name": "FDO-ACCIONES", "minimum_amount": 250000, "category": "FIC"},
    {"id": '5', "name": "FPV_BTG_PACTUAL_DINAMICA", "minimum_amount": 100000, "category": "FPV"},
]

async def insert_funds():
    await fund_collection.insert_many(FUNDS)
    print("Fondos insertados correctamente")

import asyncio
asyncio.run(insert_funds())