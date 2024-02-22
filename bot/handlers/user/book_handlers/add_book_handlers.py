from database.methods.create import add_user_book
from states.states import FSMUserBook, default_state
from filters.filters import IsCorrectBook
from services.object_store import BookObjectStore
from services.file_handling import parse_fb2, get_book_text
from lexicon.lexicon import LEXICON_RU
from utils.book_utils import get_book_id

from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext


router: Router = Router(name=__name__)


@router.message(Command(commands='add_book'), StateFilter(default_state))
async def process_add_book_command(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU[message.text])
    await state.set_state(FSMUserBook.user_book_send)


