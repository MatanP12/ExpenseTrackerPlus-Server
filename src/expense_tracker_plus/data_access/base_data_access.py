from abc import ABC, abstractmethod
from typing import Sequence, Any
from sqlmodel import Session, SQLModel


class BaseDataAccess(ABC):
    def __init__(self, session: Session):
        self.session = session

    @abstractmethod
    def get_by_id(self, pk: int) -> SQLModel | None:
        pass

    @abstractmethod
    def get_all(self) -> Sequence[SQLModel]:
        pass

    @abstractmethod
    def create(self, obj: dict[str, Any]) -> SQLModel:
        pass

    @abstractmethod
    def update(self, pk: int, obj: dict[str, Any]) -> SQLModel | None:
        pass

    @abstractmethod
    def delete(self, pk: int) -> int:
        pass
