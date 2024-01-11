from db.db_queries import *
from db.methods import execute_query
from services.file_handling import book
from keyboards.pagination_kb import create_pagination_kb

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery


router: Router = Router(name=__name__)


@router.message(Command(commands='beginning'))
async def process_beginning_command(message: Message) -> None:

    user_book_page: int = 1
    await execute_query(update_user_page, 'UPDATE',
                        user_book_page, message.from_user.id)

    await message.answer(
        text=book[user_book_page],
        reply_markup=create_pagination_kb()
    )


@router.message(Command(commands='continue'))
async def process_continue_command(message: Message) -> None:
    
    _, user_book_page = await execute_query(user_info_query, 'SELECT_ONE', message.from_user.id)

    await message.answer(
        text=book[user_book_page],
        reply_markup=create_pagination_kb(user_book_page)
    )


@router.callback_query(F.data.in_(('forward', 'backward')))
async def process_page_turning(callback: CallbackQuery) -> None:

    user_id, user_book_page = await execute_query(user_info_query, 'SELECT_ONE', callback.from_user.id)
    user_book_page += -1 if callback.data == 'backward' else 1

    await execute_query(update_user_page, 'UPDATE',
                        user_book_page, user_id)
    await callback.message.edit_text(
        text=book[user_book_page],
        reply_markup=create_pagination_kb(user_book_page)
    )