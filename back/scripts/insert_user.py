from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
from bson import ObjectId

# Configura la conexión a MongoDB
MONGO_DETAILS = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.btg_pactual
user_collection = database.get_collection("users")

USER = {
    "_id": ObjectId(),
    "id": '1',
    "name": 'Harold Duque',
    "email": 'mdukke09@gmail.com',
    "phone": '3219558919',
    "balance": 500000,
    "funds": []
}

async def insert_user():
    await user_collection.insert_one(USER)
    print("Usuario insertado correctamente")

asyncio.run(insert_user())