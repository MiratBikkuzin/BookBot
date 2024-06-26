from database.models import (
    UsersTable,
    UserBooksTable,
    BookmarksTable,
    AdminBooksTable,
    PaymentsInfoTable,
    SuccessfulPaymentsTable
)
from database.main import database

from sqlalchemy import select, and_
from itertools import chain


async def get_user_info(user_id: int) -> int:

    async with database.session as session:

        stmt = (
            select(UsersTable.num_books_to_add)
            .select_from(UsersTable)
            .where(UsersTable.user_id == user_id)
        )

        result = await session.execute(stmt)
        fetchone_result: tuple | None = result.fetchone()

        if fetchone_result:
            num_books_to_add: int = fetchone_result[0]
            return num_books_to_add
    

async def get_admin_book_info(book_id: int) -> tuple[str, int]:
    async with database.session as session:
        stmt = (
            select(AdminBooksTable.book_author, AdminBooksTable.book_title,
                   AdminBooksTable.total_page_count)
            .select_from(AdminBooksTable)
            .where(AdminBooksTable.book_id == book_id)
        )
        result = await session.execute(stmt)
        return result.fetchone()


async def get_user_book_info(user_id: int, book_id: int) -> tuple[str, str, int, int, bool] | None:
    async with database.session as session:
        stmt = (
            select(UserBooksTable.book_author, UserBooksTable.book_title,
                   UserBooksTable.total_page_count, UserBooksTable.current_page_num,
                   UserBooksTable.is_admin_book)
            .select_from(UserBooksTable)
            .where(and_(UserBooksTable.user_id == user_id,
                        UserBooksTable.book_id == book_id))
        )
        result = await session.execute(stmt)
        return result.fetchone()
    

async def get_user_books_with_bookmarks(user_id: int) -> list[tuple[str, str, str]]:
    async with database.session as session:
        stmt = (
            select(BookmarksTable.book_id, BookmarksTable.book_author, BookmarksTable.book_title)
            .select_from(BookmarksTable)
            .where(BookmarksTable.user_id == user_id)
            .distinct()
        )
        result = await session.execute(stmt)
        return result.fetchall()
    

async def get_user_book_bookmarks(user_id: int, book_id: str) -> tuple[int]:
    async with database.session as session:
        stmt = (
            select(BookmarksTable.page_number)
            .select_from(BookmarksTable)
            .where(BookmarksTable.user_id == user_id, BookmarksTable.book_id == book_id)
        )
        result = await session.execute(stmt)
        return tuple(chain.from_iterable(result.fetchall()))
    

async def get_total_bookmarks_num(user_id: int) -> int:
    async with database.session as session:
        stmt = (
            select(BookmarksTable.id)
            .select_from(BookmarksTable)
            .where(BookmarksTable.user_id == user_id)
        )
        result = await session.execute(stmt)
        return len(result.fetchall())
    

async def get_admin_books() -> list[tuple[str, str, str, int]]:
    async with database.session as session:
        stmt = (
            select(AdminBooksTable.book_id, AdminBooksTable.book_author,
                   AdminBooksTable.book_title, AdminBooksTable.total_page_count)
            .select_from(AdminBooksTable)
        )
        result = await session.execute(stmt)
        return result.fetchall()
    

async def get_user_books(user_id: int) -> list[tuple[str, str, str, int]]:
    async with database.session as session:
        stmt = (
            select(UserBooksTable.book_id, UserBooksTable.book_author,
                   UserBooksTable.book_title, UserBooksTable.total_page_count)
            .select_from(UserBooksTable)
            .where(UserBooksTable.user_id == user_id)
        )
        result = await session.execute(stmt)
        return result.fetchall()
    

async def get_num_readers_book(book_id: str) -> int:
    async with database.session as session:
        stmt = (
            select(UserBooksTable.user_id)
            .select_from(UserBooksTable)
            .where(UserBooksTable.book_id == book_id)
        )
        result = await session.execute(stmt)
        return len(result.fetchall())
    

async def get_user_invoice_id(user_id: int) -> int:
    async with database.session as session:
        stmt = (
            select(PaymentsInfoTable.invoice_id)
            .select_from(PaymentsInfoTable)
            .where(PaymentsInfoTable.user_id == user_id)
        )
        result = await session.execute(stmt)
        return result.fetchone()
    

async def check_is_invoice_id_unique(inv_id: int) -> bool:
    async with database.session as session:
        stmt1 = (
            select(PaymentsInfoTable.id)
            .select_from(PaymentsInfoTable)
            .where(PaymentsInfoTable.invoice_id == inv_id)
        )
        stmt2 = (
            select(SuccessfulPaymentsTable.id)
            .select_from(SuccessfulPaymentsTable)
            .where(SuccessfulPaymentsTable.invoice_id == inv_id)
        )
        
        result1 = await session.execute(stmt1)
        result2 = await session.execute(stmt2)

        rows_count1: int = len(result1.fetchall())
        rows_count2: int = len(result2.fetchall())

        return (False, True)[rows_count1 <= 1 and rows_count2 == 0]