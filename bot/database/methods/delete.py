from database.models import BookmarksTable
from database.main import Database

from sqlalchemy import delete


async def del_user_bookmark(user_id: int, bookmark_page: int) -> None:
    async with Database().session as session:
        stmt = (
            delete(BookmarksTable)
            .filter_by(user_id=user_id, bookmark_page=bookmark_page)
        )
        await session.execute(stmt)
        await session.commit()