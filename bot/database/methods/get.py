from database.models import UsersTable, BookmarksTable, AdminBooksTable
from database.main import Database

from sqlalchemy import select, func


async def get_user_info(user_id: int) -> tuple[int, int]:
    async with Database().session as session:
        stmt = (
            select(UsersTable.user_id, UsersTable.page)
            .select_from(UsersTable)
            .where(UsersTable.user_id == user_id)
        )
        result = await session.execute(stmt)
        return result.fetchone()
    

async def get_user_bookmarks(user_id: int) -> list[tuple[int]]:
    async with Database().session as session:
        stmt = (
            select(BookmarksTable.bookmark_page)
            .select_from(BookmarksTable)
            .where(BookmarksTable.user_id == user_id)
        )
        result = await session.execute(stmt)
        return result.fetchall()
    

async def get_admin_books(admin_book_id: int) -> tuple[str, str]:
    async with Database().session as session:
        stmt = (
            select(AdminBooksTable.file_tg_id, AdminBooksTable.book_title)
            .select_from(AdminBooksTable)
            .where(AdminBooksTable.id == admin_book_id)
        )
        result = await session.execute(stmt)
        return result.fetchall()
    

async def get_count_admin_books() -> int:
    async with Database().session as session:
        result = await session.execute(select(func.count()).select_from(AdminBooksTable))
        return int(result.fetchone()[0])