from datetime import datetime
from sqlmodel import Field, SQLModel  # type:ignore
from enum import StrEnum


tableName = "transactions"


class TransactionType(StrEnum):
    Income = "Income"
    Expense = "Expense"


class TransactionBase(SQLModel):
    description: str | None = None
    amount: int = 1
    date: datetime = datetime.now()
    bussiness: str | None = None
    type: TransactionType = TransactionType.Expense


class Transaction(TransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # Relations


class TransactionRecieve(TransactionBase):
    pass


class TransactionSend(TransactionBase):
    id: int = Field(primary_key=True)
