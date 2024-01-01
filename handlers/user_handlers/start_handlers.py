from db.db_queries import *
from db.methods import execute_query
from lexicon.lexicon import LEXICON_RU

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


router: Router = Router(name=__name__)


@router.message(CommandStart())
async def process_start_command(message: Message) -> None:

    user_id: int = message.from_user.id
    firstname: str = message.from_user.first_name

    if not await execute_query(select_user_info_query, 'SELECT_ONE', user_id):
        await execute_query(add_user_info_query, 'INSERT', user_id, 0)
        await message.answer(LEXICON_RU[message.text] % firstname)

    else:
        await message.answer(LEXICON_RU['reset_start'] % firstname)


@router.message(Command(commands='help'))
async def process_help_command(message: Message) -> None:
    await message.answer(LEXICON_RU[message.text])