from lexicon.lexicon import LEXICON_RU
from database.methods.get import get_admin_books, get_user_books
from keyboards.kb_utils import (AdminBookCallbackFactory, EditAdminBookCallbackFactory,
                                UserBookCallbackFactory, EditUserBookCallbackFactory)

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class BooksKeyboard:

    @staticmethod
    def create_choice_books_kb() -> InlineKeyboardMarkup:

        admin_books: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['choice_admin_books'],
                                                                callback_data='admin-books')
        user_books: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['choice_user_books'],
                                                                callback_data='user-books')
        
        return InlineKeyboardMarkup(inline_keyboard=[[admin_books, user_books]])
    
    @staticmethod
    async def create_admin_books_kb() -> InlineKeyboardMarkup:
        
        kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

        for book_id, book_title, page_count in await get_admin_books():
            callback_data: str = AdminBookCallbackFactory(total_page_count=page_count,
                                                          book_id=book_id).pack()
            kb_builder.row(InlineKeyboardButton(text=book_title, callback_data=callback_data))

        kb_builder.row(InlineKeyboardButton(
            text=LEXICON_RU['edit_button'],
            callback_data='edit-admin-books'
        ))

        return kb_builder.as_markup()
    
    @staticmethod
    async def create_edit_admin_books_kb() -> InlineKeyboardMarkup:
        
        kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

        for book_id, book_title, _ in await get_admin_books():
            callback_data: str = EditAdminBookCallbackFactory(book_id=book_id).pack()
            kb_builder.row(InlineKeyboardButton(
                text=f"{LEXICON_RU['del']} {book_title}",
                callback_data=callback_data
            ))

        return kb_builder.as_markup()
    
    @staticmethod
    async def create_user_books_kb(user_id: int) -> InlineKeyboardMarkup:
        
        kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

        for book_id, book_title, page_count in await get_user_books(user_id):
            callback_data: str = UserBookCallbackFactory(total_page_count=page_count,
                                                         book_id=book_id).pack()
            kb_builder.row(InlineKeyboardButton(text=book_title, callback_data=callback_data))

        return kb_builder.as_markup()
    
    @staticmethod
    def create_cancel_add_book_kb() -> InlineKeyboardMarkup:
        cancel_button: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['cancel'],
                                                                   callback_data='cancel_add_book')
        return InlineKeyboardMarkup(inline_keyboard=[[cancel_button]])