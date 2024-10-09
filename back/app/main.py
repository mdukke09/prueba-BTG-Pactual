from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import user, fund, transaction

app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/api")
app.include_router(fund.router, prefix="/api")
app.include_router(transaction.router, prefix="/api")