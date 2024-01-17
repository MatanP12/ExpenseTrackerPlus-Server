import os

from sqlmodel import Session, SQLModel, create_engine


class DatabaseManager:
    service = os.getenv("DB_SERVICE")
    postgres_url = "postgresql://postgres:1234@db/expense_tracker"
    sqllite_url = "sqlite:///expense_tracker.db"
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.init()
        return cls._instance

    def init(self):
        url = self.postgres_url if self.service else self.sqllite_url
        self.engine = create_engine(url=url, echo=True)

    def create_session(self) -> Session:
        return Session(self.engine)

    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.engine)
