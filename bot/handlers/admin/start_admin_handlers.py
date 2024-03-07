from filters.filters import IsAdmin
from keyboards.books_kb import BooksKeyboard
from lexicon.lexicon import LEXICON_RU

from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message


router: Router = Router(name=__name__)


@router.message(Command(commands='update'), IsAdmin(), StateFilter(default_state))
async def process_update_command(message: Message):
    await message.answer(
        text=LEXICON_RU[message.text],
        reply_markup=BooksKeyboard.create_selecting_admin_actions_kb()
    )


@router.message(Command(commands='update'), ~IsAdmin())
async def not_update_warning(message: Message):
    await message.answer(text=LEXICON_RU['other_update_command'])