from database.main import Database, Base

from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column


intpk = Annotated[int, mapped_column(primary_key=True)]
userid_pk = Annotated[int, mapped_column(autoincrement=False, primary_key=True)]


async def register_models():
    async with Database().session as session:
        await session.run_sync(Base.metadata.create_all)


class UsersTable(Base):
    id: intpk
    user_id: userid_pk

    page: Mapped[int]


class BookmarksTable(Base):
    id: intpk
    user_id: userid_pk

    bookmark_page: Mapped[int]


class AdminBooksTable(Base):
    id: intpk
    admin_username: Mapped[str]

    file_tg_id: Mapped[str]
    book_title: Mapped[str]