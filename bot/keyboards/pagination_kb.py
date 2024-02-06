from keyboards.kb_utils import PageTurningCallbackFactory, PageCallbackFactory
from lexicon.lexicon import LEXICON_RU

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def _pagination_kb(*callback_factories) -> InlineKeyboardMarkup:

    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    inline_buttons: list[InlineKeyboardButton] = []

    for callback_factory in callback_factories:
        callback_factory: PageTurningCallbackFactory | PageCallbackFactory

        if isinstance(callback_factory, PageTurningCallbackFactory):
            button_text: str = LEXICON_RU[callback_factory.turn_type]

        else:
            button_text: str = f'{callback_factory.page_num}/{callback_factory.page_count}'

        inline_buttons.append(InlineKeyboardButton(
            text=button_text,
            callback_data=callback_factory.pack()))

    kb_builder.row(*inline_buttons, width=3)

    return kb_builder.as_markup()
        


def create_pagination_kb(book_id: str, page_count: int, page_num: int = 1) -> InlineKeyboardMarkup:

    backward_button = PageTurningCallbackFactory(turn_type='backward', book_id=book_id)
    middle_button = PageCallbackFactory(page_num=page_num, page_count=page_count, book_id=book_id)
    forward_button = PageTurningCallbackFactory(turn_type='forward', book_id=book_id)

    if page_num == 1:
        return _pagination_kb(middle_button, forward_button)
    
    if 1 < page_num < page_count:
        return _pagination_kb(backward_button, middle_button, forward_button)
    
    else:
        return _pagination_kb(backward_button, middle_button)