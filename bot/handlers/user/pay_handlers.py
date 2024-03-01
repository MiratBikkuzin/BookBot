from keyboards.pay_kb import (
    book_price,
    five_books_price,
    ten_books_price,
    unlimited_books_price,
    PaymentKeyboards
)
from database.methods.update import update_quantity_to_add_books
from lexicon.lexicon import LEXICON_RU

from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command


router: Router = Router()


@router.message(Command(commands='top_up'))
async def process_select_quantity_for_top_up(message: Message):
    await message.answer(
        text=LEXICON_RU['top_up_quantity_text'],
        reply_markup=PaymentKeyboards.create_payment_kb()
    )