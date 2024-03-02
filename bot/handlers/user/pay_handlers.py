from keyboards.pay_kb import (
    ten_books_price,
    unlimited_books_price,
    max_tip_amount,
    tip_amounts,
    start_parameter,
    create_payment_kb
)
from database.methods.update import update_quantity_to_add_books
from config_data.config import bot_settings
from lexicon.lexicon import LEXICON_RU

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, PreCheckoutQuery
from aiogram.filters import Command


router: Router = Router()


@router.message(Command(commands='top_up'))
async def process_send_selection_quantity_for_top_up(message: Message):
    await message.answer(
        text=LEXICON_RU['top_up_quantity_text'],
        reply_markup=create_payment_kb()
    )


@router.callback_query(F.data == 'ten_books_add')
async def process_select_ten_books_to_add(callback: CallbackQuery):
    await callback.message.answer_invoice(
        title=LEXICON_RU['ten_books_invoice_title'],
        description=LEXICON_RU['invoice_description'],
        payload='10',
        provider_token=bot_settings.payment_token,
        currency='RUB',
        prices=[ten_books_price],
        max_tip_amount=max_tip_amount,
        suggested_tip_amounts=tip_amounts,
        start_parameter=start_parameter
    )
    await callback.answer()


@router.callback_query(F.data == 'unlimited_books_add')
async def process_select_unlimited_books_to_add(callback: CallbackQuery):
    await callback.message.answer_invoice(
        title=LEXICON_RU['unlimited_books_invoice_title'],
        description=LEXICON_RU['invoice_description'],
        payload='infinity',
        provider_token=bot_settings.payment_token,
        currency='RUB',
        prices=[unlimited_books_price],
        max_tip_amount=max_tip_amount,
        suggested_tip_amounts=tip_amounts,
        start_parameter=start_parameter
    )
    await callback.answer()


@router.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await pre_checkout_query.answer(ok=True)