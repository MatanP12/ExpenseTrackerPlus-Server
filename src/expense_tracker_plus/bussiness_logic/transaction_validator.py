from typing import Any

from ..utils.exeptions import InvalidFieldExeption


class TransactionValidator:
    _DESCRIPTION = "description"
    _AMOUNT = "amount"

    @classmethod
    def validate(cls, transaction_data: dict[str, Any]):
        if cls._DESCRIPTION in transaction_data and not transaction_data.get(cls._DESCRIPTION):
            raise InvalidFieldExeption(
                reason=f"The field Transaction.{cls._DESCRIPTION} cannot be empty, should be Null",
            )
        if cls._AMOUNT in transaction_data and transaction_data[cls._AMOUNT] <= 0:
            raise InvalidFieldExeption(
                reason=f"The field Transaction.{cls._AMOUNT} cannot have non-positive value",
            )
