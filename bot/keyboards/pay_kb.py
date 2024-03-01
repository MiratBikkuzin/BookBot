from lexicon.lexicon import LEXICON_RU
from aiogram.types import LabeledPrice, InlineKeyboardMarkup, InlineKeyboardButton


ten_books_price = LabeledPrice(label=LEXICON_RU['pay_label'], amount=99 * 100)
unlimited_books_price = LabeledPrice(label=LEXICON_RU['pay_label'], amount=500 * 100)

max_tip_amount: int = 80 * 100
tip_amounts: list[int] = [10 * 100, 20 * 100, 40 * 100, 80 * 100]

start_parameter: str = 'chitalkabot'


class PaymentKeyboards:

    @staticmethod
    def create_payment_kb() -> InlineKeyboardMarkup:

        ten_books_add_button = InlineKeyboardButton(text='10', callback_data='ten_books_add')
        unlimited_books_add_button = InlineKeyboardButton(text='Бесконечное количество',
                                                          callback_data='unlimited_books_add')
        
        inline_keyboard: list = [[ten_books_add_button],
                                 [unlimited_books_add_button]]

        return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

    @staticmethod
    def create_replenish_kb() -> InlineKeyboardMarkup:
        pay_button = InlineKeyboardButton(text='Заплатить', pay=True)
        back_button = InlineKeyboardButton(text=LEXICON_RU['back_button'],
                                           callback_data='back_from_replenishment')
        return InlineKeyboardMarkup(inline_keyboard=[[pay_button], [back_button]])