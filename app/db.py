import os

from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(
    os.getenv('DB_USER'),
    os.getenv('DB_PASSWORD'),
    os.getenv('DB_HOST'),
    os.getenv('DB_PORT'),
    os.getenv('DB_NAME'),
)


engine = create_engine(DATABASE_URL)

def init_db()-> None:
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    with Session(engine) as session:
        yield session