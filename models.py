from typing import Optional
from sqlalchemy.future import engine
import random
import string
from sqlmodel import Field, SQLModel, create_engine, Session, select


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
        lower_cases[random.randint(1, 26)] + upper_cases[random.randint(1, 26)]
        for _ in range(4)
    )
    return shorten_url


def add_to_db(url: str):

    url = Url(url=url, shorten_url=create_shorten_url())

    with Session(engine) as session:
        session.add(url)
        session.commit()


def get_all_url():
    with Session(engine) as session:
        return [obj for obj in session.exec(select(Url))]


def get_url(shoreten_link: str):
    with Session(engine) as session:
        url = session.exec(select(Url).where(Url.shorten_url == shoreten_link))
        return url
