from fastapi import FastAPI, Request
from .routers.transaction_router import transactions_router
from .data_access.database_manager import DatabaseManager


app = FastAPI()


def db_session(request: Request):
    return DatabaseManager().create_session()


app.include_router(transactions_router)


@app.on_event("startup")
def on_startup():
    db_manager = DatabaseManager()
    db_manager.create_db_and_tables()
