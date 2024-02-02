from lexicon.lexicon import LEXICON_RU

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def _pagination_kb(*buttons: tuple[str]) -> InlineKeyboardMarkup:

    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    kb_builder.row(*(InlineKeyboardButton(
        text=LEXICON_RU.get(button, button),
        callback_data=button) for button in buttons)
    )

    return kb_builder.as_markup()


async def create_pagination_kb(page_count: int, page: int = 1) -> InlineKeyboardMarkup:
    
    middle_button: str = f'{page}/{page_count}'

    if page == 1:
        return _pagination_kb(middle_button, 'forward')
    
    if 1 < page < page_count:
        return _pagination_kb('backward', middle_button, 'forward')
    
    else:
        return _pagination_kb('backward', middle_button)