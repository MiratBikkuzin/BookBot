from database.models import UsersTable, UserBooksTable, PaymentsInfoTable
from database.main import database

from sqlalchemy import update, and_


async def update_quantity_to_add_books(user_id: int, num_books_to_add: int) -> None:
    async with database.session as session:
        stmt = (
            update(UsersTable)
            .values(num_books_to_add=num_books_to_add)
            .where(UsersTable.user_id == user_id)
        )
        await session.execute(stmt)
        await session.commit()


async def update_book_page(user_id: int, book_id: str, new_page: int) -> None:
    async with database.session as session:
        stmt = (
            update(UserBooksTable)
            .values(current_page_num=new_page)
            .where(and_(UserBooksTable.user_id == user_id,
                        UserBooksTable.book_id == book_id))
        )
        await session.execute(stmt)
        await session.commit()


async def update_payment_info(user_id: int, inv_id: int) -> None:
    async with database.session as session:
        stmt = (
            update(PaymentsInfoTable)
            .values(invoice_id=inv_id)
            .where(PaymentsInfoTable.user_id == user_id)
        )
        await session.execute(stmt)
        await session.commit()