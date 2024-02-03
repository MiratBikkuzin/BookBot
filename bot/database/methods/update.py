from database.models import UserBooksTable
from database.main import Database

from sqlalchemy import update, and_


async def update_book_page(user_id: int, book_id: str, new_page: int) -> None:
    async with Database().session as session:
        stmt = (
            update(UserBooksTable)
            .values(current_page_num=new_page)
            .where(and_(UserBooksTable.user_id == user_id,
                        UserBooksTable.book_id == book_id))
        )
        await session.execute(stmt)
        await session.commit()