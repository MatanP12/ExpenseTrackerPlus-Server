from sqlmodel import Session, SQLModel, create_engine


class DatabaseManager:
    postgresql_url = "postgresql://postgres:1234@localhost:5432/expense_tracker"
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.init()
        return cls._instance

    def init(self):
        self.engine = create_engine(url=self.postgresql_url, echo=True)

    def create_session(self) -> Session:
        return Session(self.engine)

    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.engine)
