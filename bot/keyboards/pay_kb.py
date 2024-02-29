from lexicon.lexicon import LEXICON_RU
from aiogram.types import LabeledPrice


book_price = LabeledPrice(label=LEXICON_RU['pay_label'], amount=7 * 100)
five_books_price = LabeledPrice(label=LEXICON_RU['pay_label'], amount=30 * 100)
ten_books_price = LabeledPrice(label=LEXICON_RU['pay_label'], amount=55 * 100)
unlimited_books_price = LabeledPrice(label=LEXICON_RU['pay_label'], amount=500 * 100)