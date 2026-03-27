import os
from contextlib import contextmanager

import dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

env_file = dotenv.find_dotenv()
dotenv.load_dotenv(env_file)


class Database:
    def __init__(self):
        self.engine = create_engine(
            os.getenv("DB_CONNECTION_STRING"), echo=True
        )

    @contextmanager
    def get_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()


class Base(DeclarativeBase):
    pass
