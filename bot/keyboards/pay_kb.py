from keyboards.kb_utils import NumBooksToAddCallbackFactory, PaymentVerifCallbackFactory
from lexicon.lexicon import LEXICON_RU

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_choice_books_payment_kb(user_id: int) -> InlineKeyboardMarkup:

    five_books_add_button = InlineKeyboardButton(
        text='5',
        callback_data=NumBooksToAddCallbackFactory(user_id=user_id, num_books_to_add=5).pack()
    )
    ten_books_add_button = InlineKeyboardButton(
        text='10',
        callback_data=NumBooksToAddCallbackFactory(user_id=user_id, num_books_to_add=10).pack()
    )
    twenty_books_add_button = InlineKeyboardButton(
        text='20',
        callback_data=NumBooksToAddCallbackFactory(user_id=user_id, num_books_to_add=20).pack()
    )
    fourty_books_add_button = InlineKeyboardButton(
        text='40',
        callback_data=NumBooksToAddCallbackFactory(user_id=user_id, num_books_to_add=40).pack()
    )
        
    inline_keyboard: list = [[five_books_add_button, ten_books_add_button],
                             [twenty_books_add_button, fourty_books_add_button]]

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_payment_kb(payment_link: str, inv_id: int, price: int) -> InlineKeyboardMarkup:
    
    link_button = InlineKeyboardButton(
        text=LEXICON_RU['books_price_button'] % price,
        url=payment_link
    )
    check_payment_button = InlineKeyboardButton(
        text=LEXICON_RU['check_payment_button'],
        callback_data=PaymentVerifCallbackFactory(invoice_id=inv_id).pack()
    )

    return InlineKeyboardMarkup(inline_keyboard=[[link_button], [check_payment_button]])