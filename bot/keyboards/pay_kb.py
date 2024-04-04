from lexicon.lexicon import LEXICON_RU
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_choice_books_payment_kb() -> InlineKeyboardMarkup:

    ten_books_add_button = InlineKeyboardButton(text='10', callback_data='ten_books_add')
    unlimited_books_add_button = InlineKeyboardButton(
        text=LEXICON_RU['unlimited_books_button'],
        callback_data='unlimited_books_add'
    )
        
    inline_keyboard: list = [[ten_books_add_button],
                             [unlimited_books_add_button]]

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_payment_kb(payment_link: str, price: int) -> InlineKeyboardMarkup:
    
    link_button = InlineKeyboardButton(
        text=LEXICON_RU['books_price_button'] % price,
        url=payment_link
    )
    check_payment_button = InlineKeyboardButton(
        text=LEXICON_RU['check_payment_button'],
        callback_data='check-payment-process'
    )

    return InlineKeyboardMarkup(inline_keyboard=[[link_button], [check_payment_button]])