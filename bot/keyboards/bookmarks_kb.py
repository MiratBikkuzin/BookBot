from database.methods.get import get_user_books_with_bookmarks
from services.object_store import BookObjectStore
from keyboards.kb_utils import (BookMarkCallbackFactory, EditBookMarkCallbackFactory,
                                BookPageMarkCallbackFactory, EditBookPageMarkCallbackFactory)
from lexicon.lexicon import LEXICON_RU

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class BookmarksKeyboard:

    @staticmethod
    async def create_bookmarks_kb(user_id: int) -> InlineKeyboardMarkup:

        kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
        books: list[tuple[str, str]] = await get_user_books_with_bookmarks(user_id)

        for book_id, book_title in books:
            kb_builder.row(InlineKeyboardButton(
                text=book_title,
                callback_data=BookMarkCallbackFactory(book_id)
            ))

        kb_builder.row(
            InlineKeyboardButton(
                text=LEXICON_RU['edit_bookmarks_button'],
                callback_data='edit_bookmarks'
            ),
            InlineKeyboardButton(
                text=LEXICON_RU['cancel'],
                callback_data='cancel'
            )
        )

        return kb_builder.as_markup()
    
    @staticmethod
    async def create_edit_kb(user_id: int) -> InlineKeyboardMarkup:

        kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
        books: list[tuple[str, str]] = await get_user_books_with_bookmarks(user_id)

        for book_id, book_title in books:
            kb_builder.row(InlineKeyboardButton(
                text=f"{LEXICON_RU['del']} {book_title}",
                callback_data=EditBookMarkCallbackFactory(book_id)
            ))

        kb_builder.row(InlineKeyboardButton(
            text=LEXICON_RU['cancel'],
            callback_data='cancel'
            ))

        return kb_builder.as_markup()
    
    @staticmethod
    def back_from_bookmark_kb() -> InlineKeyboardMarkup:
        
        back_button: InlineKeyboardButton = InlineKeyboardButton(
            text=LEXICON_RU['back_bookmark_button'],
            callback_data='back_bookmark'
        )

        return InlineKeyboardMarkup(inline_keyboard=[[back_button]])