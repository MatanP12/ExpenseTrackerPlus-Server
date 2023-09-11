from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select

from ..models.db_connection import engine
from ..models.transaction_model import (
    Transaction,
    TransactionRecieve,
    TransactionSend,
    TransactionUpdate,
)

transactions_router = APIRouter(prefix="/transactions", tags=["tramsactions"])


@transactions_router.get("/", response_model=list[TransactionSend])
def get_transactions():
    with Session(engine) as session:
        transactions = session.exec(select(Transaction)).all()
        return transactions


@transactions_router.get("/{transaction_id}", response_model=TransactionSend)
def get_transaction(transaction_id: int):
    with Session(engine) as session:
        transaction = session.exec(select(Transaction).where(Transaction.id == transaction_id)).first()
        if not transaction:
            raise HTTPException(status_code=404, detail="There is no transaction with the id")
        return transaction


@transactions_router.post("/", response_model=TransactionSend)
def create_transaction(transaction: TransactionRecieve):
    with Session(engine) as session:
        db_transaction = Transaction.from_orm(transaction)
        session.add(db_transaction)
        session.commit()
        session.refresh(db_transaction)
        return db_transaction


@transactions_router.patch("/{transaction_id}", response_model=TransactionSend)
def update_transaction(transaction_id: int, transaction: TransactionUpdate):
    with Session(engine) as session:
        db_transaction = session.get(Transaction, transaction_id)
        if not db_transaction:
            raise HTTPException(status_code=404, detail="There is no transaction with the id")
        transaction_data = transaction.dict(exclude_unset=True)
        for key, value in transaction_data.items():
            setattr(db_transaction, key, value)
        session.add(db_transaction)
        session.commit()
        session.refresh(db_transaction)
        return db_transaction


@transactions_router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int):
    with Session(engine) as session:
        db_transaction = session.get(Transaction, transaction_id)
        if not db_transaction:
            raise HTTPException(status_code=404, detail="There is no transaction with the id")
        print(db_transaction)
        session.delete(db_transaction)
        session.commit()
    return "deleted"
