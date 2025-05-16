from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./dev.db"  # 또는 postgres 사용 가능
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
