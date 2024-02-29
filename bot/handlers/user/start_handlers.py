from database.methods.create import add_user
from database.methods.get import get_user_info
from lexicon.lexicon import LEXICON_RU

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


router: Router = Router(name=__name__)


@router.message(CommandStart())
async def process_start_command(message: Message) -> None:

    user_id: int = message.from_user.id
    firstname: str = message.from_user.first_name

    if not await get_user_info(user_id):
        await add_user(user_id, num_books_to_add=5)
        await message.answer(LEXICON_RU[message.text] % firstname)

    else:
        await message.answer(LEXICON_RU['reset_start'] % firstname)


@router.message(Command(commands='help'))
async def process_help_command(message: Message) -> None:
    await message.answer(LEXICON_RU[message.text])