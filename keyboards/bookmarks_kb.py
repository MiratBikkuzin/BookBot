from services.file_handling import book
from lexicon.lexicon import LEXICON_RU

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_bookmarks_kb(*args: tuple[int]) -> InlineKeyboardMarkup:

    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    for button in sorted(args):
        kb_builder.row(InlineKeyboardButton(
            text=f'{button} - {book[button][:85]}',
            callback_data=str(button)
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


def create_edit_kb(*args: tuple[int]) -> InlineKeyboardMarkup:

    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    for button in sorted(args):
        kb_builder.row(InlineKeyboardButton(
            text=f'{LEXICON_RU['del']} {button} - {book[button][:85]}',
            callback_data=f'{button}del'
        ))

    kb_builder.row(InlineKeyboardButton(
        text=LEXICON_RU['cancel'],
        callback_data='cancel'
        ))

    return kb_builder.as_markup()