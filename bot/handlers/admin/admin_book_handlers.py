from db.db_queries import add_admin_books, admin_books_query, admin_books_count_query
from db.methods import execute_query
from filters.filters import IsAdmin
from states.states import default_state, FSMAdminBook
from lexicon.lexicon import LEXICON_RU

from aiogram import Router
from aiogram.types import Message, InputMediaDocument
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext


router: Router = Router(name=__name__)


@router.message(Command(commands='update'), IsAdmin(), StateFilter(default_state))
async def process_update_command(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU[message.text])
    await state.set_state(FSMAdminBook.admin_book_document)


@router.message(Command(commands='update'), StateFilter(default_state))
async def not_update_warning(message: Message):
    await message.answer(text=LEXICON_RU['other_update_command'])