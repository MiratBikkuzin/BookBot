from database.main import Database, Base
from config_data.config import settings

from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column


intpk = Annotated[int, mapped_column(primary_key=True)]
table_args: dict[str: str] = {'schema': settings.database_schema}


async def register_models() -> None:
    async with Database().engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


class UsersTable(Base):
    __tablename__ = 'Users'
    __table_args__ = table_args

    id: Mapped[intpk]
    user_id: Mapped[int]


class BookmarksTable(Base):
    __tablename__ = 'UserBookmarks'
    __table_args__ = table_args

    id: Mapped[intpk]
    user_id: Mapped[int]

    book_title: Mapped[str]
    page_number: Mapped[int]


class AdminBooksTable(Base):
    __tablename__ = 'AdminBooks'
    __table_args__ = table_args

    id: Mapped[intpk]
    admin_username: Mapped[str]

    book_title: Mapped[str]
    total_page_count: Mapped[int]


class UserBooksTable(Base):
    __tablename__ = 'UserBooks'
    __table_args__ = table_args

    id: Mapped[intpk]
    user_id: Mapped[int]

    book_title: Mapped[str]
    total_page_count: Mapped[int]
    current_page_num: Mapped[int | None]