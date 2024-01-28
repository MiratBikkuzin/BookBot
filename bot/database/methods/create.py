from database.models import UsersTable, BookmarksTable, AdminBooksTable
from database.main import Database


async def add_user_info(user_id: int, page: int) -> None:
    async with Database().session as session:
        session.add(UsersTable(user_id=user_id, page=page))
        await session.commit()


async def add_user_bookmark(user_id: int, bookmark_page: int) -> None:
    async with Database().session as session:
        session.add(BookmarksTable(user_id=user_id, bookmark_page=bookmark_page))
        await session.commit()


async def add_admin_books(admin_username: str, admin_book_id: str, book_title: str) -> None:
    async with Database().session as session:
        session.add(AdminBooksTable(admin_username=admin_username,
                                    admin_book_id=admin_book_id,
                                    book_title=book_title))
        await session.commit()