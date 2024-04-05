from keyboards.pay_kb import create_choice_books_payment_kb, create_payment_kb
from database.methods.get import get_user_info
from database.methods.update import update_quantity_to_add_books
from utils.pay_utils import generate_payment_link, create_unique_invoice_id
from lexicon.lexicon import LEXICON_RU

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command


router: Router = Router(name=__name__)
ten_books_price: int = 99
unlimited_books_price: int = 499


@router.message(Command(commands='top_up'))
async def process_send_selection_quantity_for_top_up(message: Message):
    await message.answer(
        text=LEXICON_RU['top_up_quantity_text'],
        reply_markup=create_choice_books_payment_kb()
    )


@router.callback_query(F.data == 'ten_books_add')
async def process_select_ten_books_to_add(callback: CallbackQuery):

    user_id: int = callback.from_user.id
    inv_id: int = await create_unique_invoice_id(user_id)

    payment_link: str = generate_payment_link(
        user_id,
        num_books_to_add=10,
        price=ten_books_price,
        description='buy 10 books for additions',
        inv_id=inv_id
    )

    await callback.message.answer(
        text=LEXICON_RU['ten_books_description'],
        reply_markup=create_payment_kb(payment_link, inv_id, ten_books_price)
    )

    await callback.answer()


@router.callback_query(F.data == 'unlimited_books_add')
async def process_select_unlimited_books_to_add(callback: CallbackQuery):
    
    user_id: int = callback.from_user.id
    inv_id: int = await create_unique_invoice_id(user_id)

    payment_link: str = generate_payment_link(
        user_id,
        num_books_to_add='unlimited',
        price=unlimited_books_price,
        description='buy unlimited quantity of books for adding',
        inv_id=inv_id
    )

    await callback.message.answer(
        text=LEXICON_RU['unlimited_books_description'],
        reply_markup=create_payment_kb(payment_link, inv_id, unlimited_books_price)
    )

    await callback.answer()


# @router.pre_checkout_query()
# async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):

#     current_num_books_to_add: int | str = await get_user_info(pre_checkout_query.from_user.id)

#     if isinstance(current_num_books_to_add, str):
#         await pre_checkout_query.answer(ok=False, error_message=LEXICON_RU['error_payment_message'])

#     else:
#         await pre_checkout_query.answer(ok=True)


# @router.message(F.successful_payment)
# async def process_successful_payment(message: Message):

#     user_id: int = message.from_user.id
#     num_books_to_add: str = message.successful_payment.invoice_payload

#     if num_books_to_add != 'unlimited':
#         current_num_books_to_add: int = await get_user_info(user_id)
#         num_books_to_add: int = int(num_books_to_add)
#         num_books_to_add += current_num_books_to_add

#     await update_quantity_to_add_books(user_id, num_books_to_add)
#     await message.answer(text=LEXICON_RU['successful_payment'])