from lexicon.lexicon import LEXICON_RU
from aiogram.types import LabeledPrice, InlineKeyboardMarkup, InlineKeyboardButton


book_price = LabeledPrice(label=LEXICON_RU['pay_label'], amount=7 * 100)
five_books_price = LabeledPrice(label=LEXICON_RU['pay_label'], amount=30 * 100)
ten_books_price = LabeledPrice(label=LEXICON_RU['pay_label'], amount=55 * 100)
unlimited_books_price = LabeledPrice(label=LEXICON_RU['pay_label'], amount=500 * 100)


def create_payment_kb() -> InlineKeyboardMarkup:
    one_book_add_button = InlineKeyboardButton(text='1', callback_data='one_book_add')
    five_books_add_button = InlineKeyboardButton(text='5', callback_data='five_books_add')
    ten_books_add_button = InlineKeyboardButton(text='10', callback_data='ten_books_add')
    unlimited_books_add_button = InlineKeyboardButton(text='Бесконечное количество',
                                                      callback_data='unlimited_books_add')
    inline_keyboard: list = [[one_book_add_button, five_books_add_button, ten_books_add_button],
                             [unlimited_books_add_button]]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)