from database.methods.get import get_user_books_with_bookmarks, get_user_book_bookmarks
from services.object_store import BookObjectStore
from keyboards.kb_utils import (BookMarkCallbackFactory, EditBookMarkCallbackFactory,
                                BookPageMarkCallbackFactory, EditBookPageMarkCallbackFactory)
from lexicon.lexicon import LEXICON_RU

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class BookmarksKeyboard:

    @staticmethod
    async def create_bookmark_kb(user_id: int) -> InlineKeyboardMarkup:

        kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
        books: list[tuple[str, str]] = await get_user_books_with_bookmarks(user_id)

        for book_id, book_title in books:
            kb_builder.row(InlineKeyboardButton(
                text=book_title,
                callback_data=BookMarkCallbackFactory(book_id=book_id)
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
    async def create_edit_bookmark_kb(user_id: int) -> InlineKeyboardMarkup:

        kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
        books: list[tuple[str, str]] = await get_user_books_with_bookmarks(user_id)

        for book_id, book_title in books:
            kb_builder.row(InlineKeyboardButton(
                text=f"{LEXICON_RU['del']} {book_title}",
                callback_data=EditBookMarkCallbackFactory(book_id=book_id)
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
    
    @staticmethod
    async def create_book_page_mark_kb(user_id: int, book_id: str) -> InlineKeyboardMarkup:

        kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
        book_bookmarks: tuple[int] = await get_user_book_bookmarks(user_id, book_id)

        for page_num in sorted(book_bookmarks):
            book_page_content: str = await BookObjectStore.get_book_page_content(book_id, page_num)
            kb_builder.row(InlineKeyboardButton(
                text=f"{page_num} - {book_page_content[:85]}",
                callback_data=BookPageMarkCallbackFactory(book_id=book_id, page_number=page_num)
            ))

        return kb_builder.as_markup()

    @staticmethod
    async def create_edit_book_page_mark_kb(user_id: int, book_id: str) -> InlineKeyboardMarkup:

        kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
        book_bookmarks: tuple[int] = await get_user_book_bookmarks(user_id, book_id)

        for page_num in sorted(book_bookmarks):
            book_page_content: str = await BookObjectStore.get_book_page_content(book_id, page_num)
            kb_builder.row(InlineKeyboardButton(
                text=f"{page_num} - {book_page_content[:85]}",
                callback_data=EditBookPageMarkCallbackFactory(book_id=book_id, page_number=page_num)
            ))

        return kb_builder.as_markup()