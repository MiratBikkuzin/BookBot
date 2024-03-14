from database.main import Database, Base
from config_data.config import db_settings

from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, BigInteger


intpk = Annotated[int, mapped_column(primary_key=True)]
useridk = Annotated[int, mapped_column(BigInteger())]
table_args: dict[str: str] = {'schema': db_settings.postgres_schema}


async def register_models() -> None:
    async with Database().engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


class UsersTable(Base):
    __tablename__ = 'Users'
    __table_args__ = table_args

    id: Mapped[intpk]
    user_id: Mapped[useridk]

    num_books_to_add: Mapped[str]  # this column is a string because it can have one of two values
                                   # (the number of books to add or word "unlimited")


class BookmarksTable(Base):
    __tablename__ = 'UserBookmarks'
    __table_args__ = table_args

    id: Mapped[intpk]
    user_id: Mapped[useridk]

    book_title: Mapped[str]
    book_id: Mapped[str] = mapped_column(String(41))
    page_number: Mapped[int]


class AdminBooksTable(Base):
    __tablename__ = 'AdminBooks'
    __table_args__ = table_args

    id: Mapped[intpk]
    admin_username: Mapped[str]

    book_title: Mapped[str]
    book_id: Mapped[str] = mapped_column(String(41))
    total_page_count: Mapped[int]


class UserBooksTable(Base):
    __tablename__ = 'UserBooks'
    __table_args__ = table_args

    id: Mapped[intpk]
    user_id: Mapped[useridk]

    book_author: Mapped[str]
    book_title: Mapped[str]
    book_id: Mapped[str] = mapped_column(String(41))
    total_page_count: Mapped[int]
    current_page_num: Mapped[int]

    is_admin_book: Mapped[bool]