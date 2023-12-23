from keyboards.bookmarks_kb import create_bookmarks_kb, create_edit_kb
from keyboards.pagination_kb import create_pagination_kb
from lexicon.lexicon import LEXICON_RU
from models.db_queries import *
from models.methods import execute_query
from services.file_handling import book
from filters.filters import IsDigitCallbackData, IsDelBookmarkCallbackData

from aiogram import Router, F
from aiogram.filters import (
    CommandStart, Command,
    ChatMemberUpdatedFilter,
    KICKED, MEMBER
)
from aiogram.types import (
    Message,
    CallbackQuery,
    ChatMemberUpdated
)


router: Router = Router(name='UserRouter')


@router.message(CommandStart())
async def process_start_command(message: Message) -> None:

    user_id: int = message.from_user.id
    firstname: str = message.from_user.first_name

    if not await execute_query(select_user_info_query, 'SELECT', user_id):
        await execute_query(add_user_info_query, 'INSERT', user_id, 0)
        await message.answer(LEXICON_RU[message.text] % firstname)
        
    await message.answer(LEXICON_RU['reset_start'] % firstname)


@router.message(Command(commands='help'))
async def process_help_command(message: Message) -> None:
    await message.answer(LEXICON_RU[message.text])


@router.message(Command(commands='beginning'))
async def process_beginning_command(message: Message) -> None:

    user_book_page: int = 1
    await execute_query(update_user_page_query, 'UPDATE', user_book_page)
    user_page_text: str = book[user_book_page]

    await message.answer(
        text=user_page_text,
        reply_markup=create_pagination_kb(
            'backward',
            f'{user_book_page}/{len(book)}',
            'forward'
        )
    )


@router.message(Command(commands='continue'))
async def process_continue_command(message: Message) -> None:
    
    _, user_book_page = await execute_query(select_user_info_query, 'SELECT', message.from_user.id)
    user_page_text: str = book[user_book_page]

    await message.answer(
        text=user_page_text,
        reply_markup=create_pagination_kb(
            'backward',
            f'{user_book_page}/{len(book)}',
            'forward'
        )
    )
