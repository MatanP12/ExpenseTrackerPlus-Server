import datetime
from ...utils.transactions_type import TransactionType
from pydantic import BaseModel


class TransactionBase(BaseModel):
    description: str
    amount: float
    type: TransactionType
    date: datetime.date | None
    business: str | None


class TransactionRecieve(TransactionBase):
    pass


class TransactionSend(TransactionBase):
    id: int
    date: datetime.date
    business: str


class TransactionUpdate(TransactionBase):
    description: str | None
    amount: float | None
    type: TransactionType | None
