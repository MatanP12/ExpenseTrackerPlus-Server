from sqlmodel import Session, create_engine, SQLModel


class DatabaseManager:
    _sqlite_file_name = "database.db"
    _sqlite_url = f"sqlite:///{_sqlite_file_name}"
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.init()
        return cls._instance

    def init(self):
        self.engine = create_engine(url=self._sqlite_url, echo=True)

    def create_session(self) -> Session:
        return Session(self.engine)

    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.engine)
