from database.methods.get import get_user_bookmarks
from services.s3_file_handling import get_book_s3
from keyboards.keyboard_utils import BookmarksCallbackFactory, DelBookmarksCallbackFacotry
from lexicon.lexicon import LEXICON_RU

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class BookmarkFactory:

    @staticmethod
    async def create_bookmarks_kb(user_id: int, book_title: str) -> InlineKeyboardMarkup:

        kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
        book: dict[int: str] = await get_book_s3(book_title, user_id)

        for button in sorted(await get_user_bookmarks(user_id, book_title)):
            kb_builder.row(InlineKeyboardButton(
                text=f'{button} - {book[button][:85]}',
                callback_data=BookmarksCallbackFactory(page_number=button,
                                                       book_title=book_title).pack()
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
    async def create_edit_kb(user_id: int, book_title: str) -> InlineKeyboardMarkup:

        kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
        book: dict[int: str] = await get_book_s3(book_title, user_id)

        for button in sorted(await get_user_bookmarks(user_id, book_title)):
            kb_builder.row(InlineKeyboardButton(
                text=f"{LEXICON_RU['del']} {button} - {book[button][:85]}",
                callback_data=DelBookmarksCallbackFacotry(page_number=button,
                                                          book_title=book_title).pack()
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