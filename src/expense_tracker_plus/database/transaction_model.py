import datetime

from sqlmodel import Field, SQLModel  # type:ignore

from ..utils.transactions_type import TransactionType


class DatabaseTransaction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str
    amount: float
    date: datetime.date = datetime.date.today()
    business: str = ""
    type: TransactionType
