from database.models import UsersTable, BookmarksTable, AdminBooksTable, UserBooksTable
from database.main import Database


async def add_user_info(user_id: int) -> None:
    async with Database().session as session:
        session.add(UsersTable(user_id=user_id))
        await session.commit()


async def add_user_bookmark(user_id: int, book_title: str, page_number: int) -> None:
    async with Database().session as session:
        session.add(BookmarksTable(user_id, book_title, page_number))
        await session.commit()


async def add_admin_book(admin_username: str, book_title: str, page_count: int) -> None:
    async with Database().session as session:
        session.add(AdminBooksTable(admin_username, book_title, page_count)) 
        await session.commit()


async def add_user_book(user_id: int, book_title: str, page_count: int,
                        is_admin_book: bool = False) -> None:
    async with Database().session as session:
        session.add(UserBooksTable(user_id, book_title, page_count, 0, is_admin_book))
        await session.commit()