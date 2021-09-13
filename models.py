from typing import Optional
from sqlalchemy.future import engine
import random
import string
from sqlmodel import Field, SQLModel, create_engine, Session


sqlite_file_url = "sqlite:///app.db"

engine = create_engine(sqlite_file_url, echo=False)


class Url(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    url: str = Field(max_length=500)
    shorten_url: str = Field(max_length=50)


def create_table():
    SQLModel.metadata.create_all(engine)


def create_shorten_url():
    lower_cases = string.ascii_lowercase
    upper_cases = string.ascii_uppercase
    shorten_url = "".join(
        lower_cases[random.randint(0, 26)] + upper_cases[random.randint(0, 26)]
        for _ in range(4)
    )
    return shorten_url


create_shorten_url()


def add_to_db(url: str):

    url = Url(url=url, shorten_url=create_shorten_url(url=url))

    with Session(engine) as session:
        session.add(url)
        session.commit()
