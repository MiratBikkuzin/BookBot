from database.methods.get import get_user_info
from database.methods.update import update_user_page
from services.file_handling import book
from keyboards.pagination_kb import create_pagination_kb

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery


router: Router = Router(name=__name__)


@router.message(Command(commands='beginning'))
async def process_beginning_command(message: Message) -> None:

    user_book_page: int = 1
    await update_user_page(new_page=user_book_page, user_id=message.from_user.id)

    await message.answer(
        text=book[user_book_page],
        reply_markup=create_pagination_kb()
    )


@router.message(Command(commands='continue'))
async def process_continue_command(message: Message) -> None:
    
    _, user_book_page = await get_user_info(user_id=message.from_user.id)

    await message.answer(
        text=book[user_book_page],
        reply_markup=create_pagination_kb(user_book_page)
    )


@router.callback_query(F.data.in_(('forward', 'backward')))
async def process_page_turning(callback: CallbackQuery) -> None:

    user_id, user_book_page = await get_user_info(user_id=callback.from_user.id)
    user_book_page += -1 if callback.data == 'backward' else 1

    await update_user_page(new_page=user_book_page, user_id=user_id)
    
    await callback.message.edit_text(
        text=book[user_book_page],
        reply_markup=create_pagination_kb(user_book_page)
    )