from lexicon.lexicon import LEXICON_RU

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_pagination_kb(*buttons: tuple[str]) -> InlineKeyboardMarkup:

    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    kb_builder.row(*(InlineKeyboardButton(
        text=LEXICON_RU.get(button, button),
        callback_data=button) for button in buttons)
    )

    return kb_builder.as_markup()