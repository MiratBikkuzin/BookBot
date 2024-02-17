from database.models import BookmarksTable, AdminBooksTable, UserBooksTable
from database.main import database

from sqlalchemy import delete, and_


async def del_user_bookmark(user_id: int, book_id: str, page_number: int) -> None:
    async with database.session as session:
        stmt = (
            delete(BookmarksTable)
            .where(and_(BookmarksTable.user_id == user_id, BookmarksTable.book_id == book_id,
                        BookmarksTable.page_number == page_number))
        )
        await session.execute(stmt)
        await session.commit()


async def del_admin_book(admin_username: str, admin_tg_id: int,
                         book_title: str, book_id: str) -> None:
    
    async with database.session as session:
        first_stmt = (
            delete(AdminBooksTable)
            .where(and_(AdminBooksTable.admin_username == admin_username,
                        AdminBooksTable.book_id == book_id))
        )
        second_stmt = (
            delete(UserBooksTable)
            .where(and_(UserBooksTable.is_admin_book, UserBooksTable.book_id == book_id))
        )
        await session.execute(first_stmt)
        await session.execute(second_stmt)
        await session.commit()


async def del_user_book(user_id: int, book_title: str, book_id: str) -> None:
    
    async with database.session as session:
        stmt = (
            delete(UserBooksTable)
            .where(and_(UserBooksTable.user_id == user_id, UserBooksTable.book_id == book_id))
        )
        await session.execute(stmt)
        await session.commit()