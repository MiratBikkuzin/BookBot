from database.models import UsersTable, BookmarksTable, AdminBooksTable, UserBooksTable
from database.main import Database
from utils.book_utils import get_book_id


async def add_user(user_id: int) -> None:
    async with Database().session as session:
        session.add(UsersTable(user_id=user_id))
        await session.commit()


async def add_user_bookmark(user_id: int, book_title: str, page_number: int) -> None:
    async with Database().session as session:
        session.add(BookmarksTable(user_id=user_id, book_title=book_title,
                                   book_id=get_book_id(book_title), page_number=page_number))
        await session.commit()


async def add_admin_book(admin_username: str, book_title: str, page_count: int) -> None:
    async with Database().session as session:
        session.add(AdminBooksTable(admin_username=admin_username, book_title=book_title,
                                    book_id=get_book_id(book_title), total_page_count=page_count)) 
        await session.commit()


async def add_user_book(user_id: int, book_title: str, page_count: int,
                        is_admin_book: bool = False) -> None:
    async with Database().session as session:
        session.add(UserBooksTable(user_id=user_id, book_title=book_title,
                                   book_id=get_book_id(book_title), total_page_count=page_count,
                                   current_page_num=0, is_admin_book=is_admin_book))
        await session.commit()