from sqlmodel import SQLModel, Session, create_engine

engine = create_engine("postgresql://gsusadmin:jesu0192@localhost/mydb")

def init_db()-> None:
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    with Session(engine) as session:
        yield session