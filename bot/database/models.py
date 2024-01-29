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
    __tablename__ = 'UsersInfo'
    __table_args__ = table_args

    id: Mapped[intpk]
    user_id: Mapped[int]

    page: Mapped[int]


class BookmarksTable(Base):
    __tablename__ = 'UsersBookmarks'
    __table_args__ = table_args

    id: Mapped[intpk]
    user_id: Mapped[str]

    bookmark_page: Mapped[int]


class AdminBooksTable(Base):
    __tablename__ = 'AdminBooks'
    __table_args__ = table_args

    id: Mapped[intpk]
    admin_username: Mapped[str]

    admin_book_id: Mapped[str]
    book_title: Mapped[str]