from database.models import (
    UsersTable,
    BookmarksTable,
    AdminBooksTable,
    UserBooksTable,
    PaymentsInfoTable,
    SuccessfulPaymentsTable
)
from database.main import database


async def add_user(user_id: int, num_books_to_add: int) -> None:
    async with database.session as session:
        session.add(UsersTable(user_id=user_id, num_books_to_add=num_books_to_add))
        await session.commit()


async def add_user_bookmark(user_id: int, book_id: str, book_author: str,
                            book_title: str, page_number: int) -> None:
    async with database.session as session:
        session.add(BookmarksTable(user_id=user_id, book_author=book_author, book_title=book_title,
                                   book_id=book_id, page_number=page_number))
        await session.commit()


async def add_admin_book(admin_username: str, book_id: str, book_author: str,
                         book_title: str, page_count: int) -> None:
    async with database.session as session:
        session.add(AdminBooksTable(admin_username=admin_username, book_author=book_author,
                                    book_title=book_title, book_id=book_id,
                                    total_page_count=page_count))
        await session.commit()


async def add_user_book(user_id: int, book_id: str, book_author: str, book_title: str,
                        page_count: int, is_admin_book: bool = False) -> None:
    async with database.session as session:
        session.add(UserBooksTable(user_id=user_id, book_author=book_author, book_title=book_title,
                                   book_id=book_id, total_page_count=page_count,
                                   current_page_num=1, is_admin_book=is_admin_book))
        await session.commit()


async def add_user_payment_info(user_id: int, inv_id: int) -> None:
    async with database.session as session:
        session.add(PaymentsInfoTable(user_id=user_id, invoice_id=inv_id))
        await session.commit()


async def add_successful_payment_id(inv_id: int) -> None:
    async with database.session as session:
        session.add(SuccessfulPaymentsTable(invoice_id=inv_id))
        await session.commit()