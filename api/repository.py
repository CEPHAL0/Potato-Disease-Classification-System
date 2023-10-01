from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from datetime import datetime


class Base(DeclarativeBase):
    created_at: datetime = mapped_column(default=datetime.now)


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()


def get_db():
    engine = create_engine("sqlite://./database.db", echo=True)
    with Session(engine) as session:
        yield session
