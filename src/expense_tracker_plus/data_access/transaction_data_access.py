from sqlmodel import SQLModel, select
from ..database.transaction_model import DatabaseTransaction
from typing import Any, Sequence
from ..utils.exeptions import ObjectNotFoundExeption
from .base_data_access import BaseDataAccess


class TransactionDataAccess(BaseDataAccess):
    def get_by_id(self, pk: int) -> SQLModel | None:
        res = self.session.get(DatabaseTransaction, pk)
        if not res:
            raise ObjectNotFoundExeption(object_id=pk, class_name="Transaction")
        return res

    def get_all(self) -> Sequence[SQLModel]:
        return self.session.exec(select(DatabaseTransaction)).all()

    def create(self, obj: dict[str, Any]) -> SQLModel:
        transaction = DatabaseTransaction(**obj)
        self.session.add(transaction)
        self.session.commit()
        self.session.refresh(transaction)
        return transaction

    def update(self, pk: int, obj: dict[str, Any]) -> SQLModel | None:
        transaction = self.get_by_id(pk)
        for field, value in obj.items():
            setattr(transaction, field, value)
        self.session.add(transaction)
        self.session.commit()
        self.session.refresh(transaction)
        return transaction

    def delete(self, pk: int) -> int:
        transaction = self.get_by_id(pk=pk)
        self.session.delete(transaction)
        self.session.commit()
        return pk


# class TransactionDataAccess:
#     def __init__(self, session: Session) -> None:
#         self.session = session

#     def get_all_transactions(self) -> list[DatabaseTransaction]:
#         res = self.session.exec(select(DatabaseTransaction)).all()
#         return res

#     def get_transaction(self, pk: int) -> DatabaseTransaction | None:
#         res = self.session.get(DatabaseTransaction, pk)
#         if not res:
#             raise ObjectNotFoundExeption(object_id=pk)
#         return res

#     def create_transaction(self, new_transaction: dict[str, Any]) -> DatabaseTransaction:
#         db_transaction = DatabaseTransaction(**new_transaction)
#         self.session.add(db_transaction)
#         self.session.commit()
#         self.session.refresh(db_transaction)
#         return db_transaction

#     def update_transaction(
#         self, transaction_id: int, transactions_attributes_dict: dict[str, Any]
#     ) -> DatabaseTransaction | None:
#         db_transaction = self.get_transaction(transaction_id)
#         for field, value in transactions_attributes_dict.items():
#             setattr(db_transaction, field, value)
#         self.session.add(db_transaction)
#         self.session.commit()
#         self.session.refresh(db_transaction)
#         return db_transaction

#     def delete_transaction(self, transaction_id: int):
#         self.session.delete(self.get_transaction(transaction_id))
#         self.session.commit()
#         return transaction_id
