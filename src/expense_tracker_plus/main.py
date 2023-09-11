from fastapi import FastAPI

from .models.db_connection import create_db_and_tables
from .routes.transaction_router import transactions_router

app = FastAPI()

app.include_router(transactions_router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def read_root():
    return {"Hello": "World"}
