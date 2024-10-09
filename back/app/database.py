from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = AsyncIOMotorClient(MONGO_URL)
database = client.btg_pactual

user_collection = database.get_collection("users")
fund_collection = database.get_collection("funds")
transaction_collection = database.get_collection("transactions")

# Función para obtener la colección de usuarios
def get_user_collection():
    return user_collection

# Función para obtener la colección de fondos
def get_fund_collection():
    return fund_collection

# Función para obtener la colección de transacciones
def get_transaction_collection():
    return transaction_collection