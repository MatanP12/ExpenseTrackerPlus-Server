import datetime
from enum import StrEnum

from sqlmodel import Field, SQLModel  # type:ignore


class TransactionType(StrEnum):
    Income = "Income"
    Expense = "Expense"


class TransactionBase(SQLModel):
    description: str | None = None
    amount: float = 1
    date: datetime.date | None = datetime.date.today()
    business: str | None = None
    type: TransactionType = TransactionType.Expense


class Transaction(TransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # Relations


class TransactionRecieve(TransactionBase):
    type: TransactionType = TransactionType.Expense


class TransactionSend(TransactionBase):
    id: int = Field(primary_key=True)


class TransactionUpdate(TransactionBase):
    description: str | None = None
    date: datetime.date | None = None
    business: str | None = None
