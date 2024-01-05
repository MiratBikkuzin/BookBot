from db.db_queries import add_admin_books, admin_books_query, admin_books_count_query
from db.methods import execute_query
from filters.filters import IsAdmin, IsCorrectDocumentFormat
from states.states import default_state, FSMAdminBook
from services.file_handling import book, prepare_book
from lexicon.lexicon import LEXICON_RU

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext


router: Router = Router(name=__name__)


@router.message(Command(commands='update'), IsAdmin(), StateFilter(default_state))
async def process_update_command(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU[message.text])
    await state.set_state(FSMAdminBook.admin_book_title)


@router.message(Command(commands='update'), ~IsAdmin(), StateFilter(default_state))
async def not_update_command_warning(message: Message):
    await message.answer(text=LEXICON_RU['other_update_command'])


@router.message(IsAdmin(), StateFilter(FSMAdminBook.admin_book_title), F.text)
async def admin_book_title_send(message: Message, state: FSMContext):
    book[message.text] = {}
    await message.answer(text=LEXICON_RU['admin_sent_book_title'])
    await state.set_state(FSMAdminBook.admin_book_document)


@router.message(StateFilter(FSMAdminBook.admin_book_title), ~F.text)
async def not_admin_book_title_warning(message: Message):
    await message.answer(text=LEXICON_RU['other_admin_sent_book_title'])