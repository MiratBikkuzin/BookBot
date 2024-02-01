from database.models import BookmarksTable, AdminBooksTable, UserBooksTable
from database.main import Database
from services.s3_file_handling import delete_book_s3

from sqlalchemy import delete, and_


async def del_user_bookmark(user_id: int, book_title: str, page_number: int) -> None:
    async with Database().session as session:
        stmt = (
            delete(BookmarksTable)
            .where(and_(BookmarksTable.user_id == user_id, BookmarksTable.book_title == book_title,
                        BookmarksTable.page_number == page_number))
        )
        await session.execute(stmt)
        await session.commit()


async def del_admin_book(admin_username: str, admin_user_id: int, book_title: str) -> None:
    
    async with Database().session as session:
        first_stmt = (
            delete(AdminBooksTable)
            .where(and_(AdminBooksTable.admin_username == admin_username,
                        AdminBooksTable.book_title == book_title))
        )
        second_stmt = (
            delete(UserBooksTable)
            .where(and_(UserBooksTable.is_admin_book, UserBooksTable.book_title == book_title))
        )
        await session.execute(first_stmt)
        await session.execute(second_stmt)
        await session.commit()

    await delete_book_s3(book_title, admin_user_id, True)


async def del_user_book(user_id: int, book_title: str) -> None:
    
    async with Database().session as session:
        stmt = (
            delete(UserBooksTable)
            .where(and_(UserBooksTable.user_id == user_id, UserBooksTable.book_title == book_title))
        )
        await session.execute(stmt)
        await session.commit()

    await delete_book_s3(book_title, user_id)