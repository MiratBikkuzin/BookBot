from keyboards.pay_kb import create_choice_books_payment_kb, create_payment_kb
from database.methods.create import add_successful_payment_id
from database.methods.get import get_user_info, check_is_invoice_id_unique
from database.methods.update import update_quantity_to_add_books
from utils.pay_utils import generate_payment_link, create_unique_invoice_id, is_payment_success
from keyboards.kb_utils import NumBooksToAddCallbackFactory, PaymentVerifCallbackFactory
from utils.aiohttp_utils import AiohttpSingleton
from lexicon.lexicon import LEXICON_RU

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command


router: Router = Router(name=__name__)
ru_books_prices: dict[int: int] = {
    5: 55,
    10: 99,
    20: 185,
    40: 350
}


@router.message(Command(commands='top_up'))
async def process_send_selection_quantity_for_top_up(message: Message):
    await message.answer(
        text=LEXICON_RU['top_up_quantity_text'],
        reply_markup=create_choice_books_payment_kb(message.from_user.id)
    )


@router.callback_query(NumBooksToAddCallbackFactory.filter())
async def process_select_books_to_add(callback: CallbackQuery,
                                      callback_data: NumBooksToAddCallbackFactory):
    
    user_id, num_books_to_add = callback_data.user_id, callback_data.num_books_to_add
    price: int = ru_books_prices[num_books_to_add]
    inv_id: int = await create_unique_invoice_id(user_id)

    payment_link: str = generate_payment_link(
        user_id,
        num_books_to_add=num_books_to_add,
        price=price,
        description=f'buy {num_books_to_add} books to additions',
        inv_id=inv_id
    )

    await callback.message.answer(
        text=LEXICON_RU['add_books_description'] % num_books_to_add,
        reply_markup=create_payment_kb(payment_link, inv_id, price)
    )
    await callback.answer()


@router.callback_query(PaymentVerifCallbackFactory.filter())
async def process_payment_verification(callback: CallbackQuery,
                                       callback_data: PaymentVerifCallbackFactory):
    
    inv_id: int = callback_data.invoice_id

    if await check_is_invoice_id_unique(inv_id):
    
        payment_info: tuple | None = await is_payment_success(inv_id, AiohttpSingleton.session)

        if payment_info:

            await add_successful_payment_id(inv_id)

            num_books_to_add, user_id = payment_info

            current_num_books_to_add: int = await get_user_info(user_id)
            num_books_to_add += current_num_books_to_add

            await update_quantity_to_add_books(user_id, num_books_to_add)
            await callback.message.answer(text=LEXICON_RU['successful_payment'])
            await callback.answer()

        else:
            await callback.answer(text=LEXICON_RU['error_payment_message'], show_alert=True)

    else:
        await callback.answer(text=LEXICON_RU['reverification_error'], show_alert=True)
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