from typing import Optional
from sqlalchemy.future import engine
import random
import string
from sqlmodel import Field, SQLModel, create_engine, Session, select


sqlite_file_url = "sqlite:///data/app.db"

engine = create_engine(sqlite_file_url, echo=False)


class ShoretenUrl:
    url: str


class Url(SQLModel, table=True):
    """
    This is the url table that stores the url and the shorten url

    """

    id: Optional[int] = Field(default=None, primary_key=True)
    url: str = Field(max_length=500)
    shorten_url: str = Field(
        max_length=50,
    )


def create_table():
    """
    creates the table if it doesn't exist
    """
    SQLModel.metadata.create_all(engine)


def getFullUrl(url: str) -> Url:
    """
    this returns a url object

    """
    with Session(engine) as session:
        url = session.exec(select(Url).where(Url.url == url))
        return url.first()


def getFullUrlByShorten(shoreten_link: str) -> Url:
    """
    get a shorten url from the data base

    """
    with Session(engine) as session:
        url = session.exec(select(Url).where(Url.shorten_url == shoreten_link))
        return url.first()


def create_shorten_url() -> ShoretenUrl:
    """
    returns a randomly generated string of length 4
    """
    chars = string.ascii_letters
    slug = "".join(random.choice(chars) for _ in range(5))
    if getFullUrlByShorten(shoreten_link=slug):
        return create_shorten_url()
    return slug


def add_to_db(url: str):
    """
    add url to the database

    """
    if url_ := getFullUrl(url=url):
        return url_.shorten_url
    else:
        with Session(engine) as session:
            make_shorten_url = create_shorten_url()
            url = Url(url=url, shorten_url=make_shorten_url)
            session.add(url)
            session.commit()
            return make_shorten_url


def get_all_url() -> Url:
    """
    returns all url objects from the db
    """
    with Session(engine) as session:
        return [obj for obj in session.exec(select(Url))]
