from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from ...data_access.database_manager import DatabaseManager
from ...data_access.transaction_data_access import TransactionDataAccess
from ...utils.exeptions import ObjectNotFoundExeption, InvalidFieldExeption
from ..models.transaction_model import TransactionRecieve, TransactionSend, TransactionUpdate
from ...bussiness_logic.transaction_validator import TransactionValidator
from ...utils.exeptions import InvalidFieldExeption


def get_db_session():
    session: Session = DatabaseManager().create_session()
    try:
        yield session
    finally:
        session.close()


transactions_router = APIRouter(prefix="/transactions", tags=["transactions"])


@transactions_router.get(path="/", response_model=list[TransactionSend])
def get_transactions(session: Session = Depends(dependency=get_db_session)):
    transactions = TransactionDataAccess(session=session).get_all()
    return transactions


@transactions_router.get(path="/{transaction_id}", response_model=TransactionSend)
def get_transaction(transaction_id: int, session: Session = Depends(get_db_session)):
    try:
        transaction = TransactionDataAccess(session=session).get_by_id(pk=transaction_id)
        return transaction
    except ObjectNotFoundExeption as error:
        raise HTTPException(status_code=404, detail=error.reason)


@transactions_router.post(path="/", response_model=TransactionSend)
def create_transaction(transaction: TransactionRecieve, session: Session = Depends(get_db_session)):
    transaction_dict = transaction.dict(exclude_unset=True)
    try:
        TransactionValidator.validate(transaction_data=transaction_dict)
        created_transaction = TransactionDataAccess(session=session).create(obj=transaction_dict)
        return created_transaction
    except InvalidFieldExeption as error:
        raise HTTPException(status_code=400, detail=error.reason)


@transactions_router.patch(path="/{transaction_id}", response_model=TransactionSend)
def update_transaction(transaction_id: int, transaction: TransactionUpdate, session: Session = Depends(get_db_session)):
    transaction_dict = transaction.dict(exclude_unset=True)
    try:
        TransactionValidator.validate(transaction_data=transaction_dict)
        updated_transaction = TransactionDataAccess(session=session).update(pk=transaction_id, obj=transaction_dict)
        return updated_transaction
    except InvalidFieldExeption as error:
        raise HTTPException(status_code=400, detail=error.reason)
    except ObjectNotFoundExeption as error:
        raise HTTPException(status_code=404, detail=error.reason)


@transactions_router.delete(path="/{transaction_id}")
def delete_transaction(transaction_id: int, session: Session = Depends(get_db_session)):
    try:
        deleted_transaction_id = TransactionDataAccess(session=session).delete(pk=transaction_id)
        return deleted_transaction_id
    except ObjectNotFoundExeption as error:
        raise HTTPException(status_code=404, detail=error.reason)
