from services.object_store import BookObjectStore
from keyboards.kb_utils import (BookMarkCallbackFactory, EditBookMarkCallbackFactory,
                                BookPageMarkCallbackFactory, EditBookPageMarkCallbackFactory,
                                BackPageMarkCallbackFactory)
from lexicon.lexicon import LEXICON_RU

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class BookmarksKeyboard:

    @staticmethod
    async def create_bookmark_kb(books: list[tuple[str, str, str]]) -> InlineKeyboardMarkup:

        kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

        for book_id, book_author, book_title in books:
            kb_builder.row(InlineKeyboardButton(
                text=f'{book_title} ({book_author})',
                callback_data=BookMarkCallbackFactory(book_id=book_id).pack()
            ))

        kb_builder.row(
            InlineKeyboardButton(
                text=LEXICON_RU['edit_button'],
                callback_data='edit_bookmarks'
            ))

        return kb_builder.as_markup()
    
    @staticmethod
    async def create_edit_bookmark_kb(books: list[tuple[str, str, str]]) -> InlineKeyboardMarkup:

        kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

        for book_id, book_author, book_title in books:
            kb_builder.row(InlineKeyboardButton(
                text=f"{LEXICON_RU['del']} {book_title} ({book_author})",
                callback_data=EditBookMarkCallbackFactory(book_id=book_id).pack()
            ))

        kb_builder.row(InlineKeyboardButton(
            text=LEXICON_RU['cancel'],
            callback_data='cancel_edit_bookmarks'
        ))

        return kb_builder.as_markup()
    
    @staticmethod
    def back_from_bookmark_content_kb(book_id: str) -> InlineKeyboardMarkup:
        
        back_button: InlineKeyboardButton = InlineKeyboardButton(
            text=LEXICON_RU['back_button'],
            callback_data=BackPageMarkCallbackFactory(book_id=book_id).pack()
        )

        return InlineKeyboardMarkup(inline_keyboard=[[back_button]])
    
    @staticmethod
    async def create_book_page_mark_kb(book_id: str,
                                       book_bookmarks: tuple[int]) -> InlineKeyboardMarkup:

        kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

        for page_num in sorted(book_bookmarks):
            page_content: str = await BookObjectStore.get_book_page_content(book_id, page_num)
            page_content: str = page_content[:85].replace('\n', ' ')
            kb_builder.row(InlineKeyboardButton(
                text=f"{page_num} - {page_content}",
                callback_data=BookPageMarkCallbackFactory(book_id=book_id,
                                                          page_number=page_num).pack()
            ))

        kb_builder.row(InlineKeyboardButton(
            text=LEXICON_RU['back_from_bookmarks_list'],
            callback_data='back_from_bookmarks'
        ))

        return kb_builder.as_markup()

    @staticmethod
    async def create_edit_book_page_mark_kb(book_id: str,
                                            book_bookmarks: tuple[int]) -> InlineKeyboardMarkup:

        kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

        for page_num in sorted(book_bookmarks):
            page_content: str = await BookObjectStore.get_book_page_content(book_id, page_num)
            page_content: str = page_content[:85].replace('\n', ' ')
            kb_builder.row(InlineKeyboardButton(
                text=f"{LEXICON_RU['del']} {page_num} - {page_content}",
                callback_data=EditBookPageMarkCallbackFactory(book_id=book_id,
                                                              page_number=page_num).pack()
            ))

        kb_builder.row(InlineKeyboardButton(
            text=LEXICON_RU['back_from_bookmarks_list'],
            callback_data='back_from_edit_bookmarks'
        ))

        return kb_builder.as_markup()