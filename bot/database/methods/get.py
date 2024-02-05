from database.models import UsersTable, UserBooksTable, BookmarksTable, AdminBooksTable
from database.main import Database

from sqlalchemy import select, and_
from itertools import chain


async def get_user(user_id: int) -> tuple[int]:
    async with Database().session as session:
        stmt = (
            select(UsersTable.user_id)
            .select_from(UsersTable)
            .where(UsersTable.user_id == user_id)
        )
        result = await session.execute(stmt)
        return result.fetchone()
    

async def get_admin_book_info(book_id: int) -> tuple[str, int]:
    async with Database().session as session:
        stmt = (
            select(AdminBooksTable.book_title, AdminBooksTable.total_page_count)
            .select_from(AdminBooksTable)
            .where(AdminBooksTable.book_id == book_id)
        )
        result = await session.execute(stmt)
        return result.fetchone()


async def get_user_book_info(user_id: int, book_id: int) -> tuple[str, int, int, bool] | None:
    async with Database().session as session:
        stmt = (
            select(UserBooksTable.book_title, UserBooksTable.total_page_count,
                   UserBooksTable.current_page_num, UserBooksTable.is_admin_book)
            .select_from(UserBooksTable)
            .where(and_(UserBooksTable.user_id == user_id,
                        UserBooksTable.book_id == book_id))
        )
        result = await session.execute(stmt)
        return result.fetchone()
    

async def get_user_bookmarks(user_id: int, book_id: int) -> tuple[int]:
    async with Database().session as session:
        stmt = (
            select(BookmarksTable.page_number)
            .select_from(BookmarksTable)
            .where(and_(BookmarksTable.user_id == user_id,
                        BookmarksTable.book_id == book_id))
        )
        result = await session.execute(stmt)
        return tuple(chain.from_iterable(result.fetchall()))
    

async def get_admin_books() -> list[tuple[str, str, int]]:
    async with Database().session as session:
        stmt = (
            select(AdminBooksTable.book_id, AdminBooksTable.book_title,
                   AdminBooksTable.total_page_count)
            .select_from(AdminBooksTable)
        )
        result = await session.execute(stmt)
        return result.fetchall()
    

async def get_user_books(user_id: int) -> list[tuple[str, str, int]]:
    async with Database().session as session:
        stmt = (
            select(UserBooksTable.book_id, UserBooksTable.book_title,
                   UserBooksTable.total_page_count)
            .select_from(UserBooksTable)
            .where(UserBooksTable.user_id == user_id)
        )
        result = await session.execute(stmt)
        return result.fetchall()