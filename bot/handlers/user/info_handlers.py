from database.methods.get import get_user_books, get_user_info, get_total_bookmarks_num
from utils.utils import get_profile_command_text
from lexicon.lexicon import LEXICON_RU

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router: Router = Router(name=__name__)


@router.message(Command(commands='profile'))
async def process_profile_command(message: Message):

    name: str = message.from_user.full_name
    user_id: int = message.from_user.id

    books_num: int = len(await get_user_books(user_id))
    num_books_to_add: int | str = await get_user_info(user_id)
    bookmarks_num: int = await get_total_bookmarks_num(user_id)

    result: str = get_profile_command_text(name, user_id, books_num, num_books_to_add, bookmarks_num)
    
    await message.answer(text=result)


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON_RU[message.text])