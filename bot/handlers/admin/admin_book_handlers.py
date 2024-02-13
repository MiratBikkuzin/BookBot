from database.methods.create import add_admin_book
from filters.filters import IsAdmin, IsCorrectAdminBook
from states.states import FSMAdminBook, default_state
from services.object_store import BookObjectStore
from services.file_handling import parse_fb2, get_book_text
from lexicon.lexicon import LEXICON_RU
from utils.book_utils import get_book_id

from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext


router: Router = Router(name=__name__)


@router.message(Command(commands='update'), IsAdmin(), StateFilter(default_state))
async def process_update_command(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU[message.text])
    await state.set_state(FSMAdminBook.admin_book_send)


@router.message(Command(commands='update'), ~IsAdmin())
async def not_update_warning(message: Message):
    await message.answer(text=LEXICON_RU['other_update_command'])


@router.message(StateFilter(FSMAdminBook.admin_book_send), IsCorrectAdminBook())
async def admin_send_book(message: Message, bot: Bot, book_file_id: str, book_title: str,
                          file_format: str, state: FSMContext):
    
    book_id: str = get_book_id(book_title.lower())

    if await BookObjectStore.check_book_in_stock(book_id, is_admin=True):
        await message.answer(text=LEXICON_RU['admins_book_in_stock_warning'])

    else:

        await message.answer(text=LEXICON_RU['wait_admin_book_download'])

        book_text: str = get_book_text(await bot.download(book_file_id))

        if file_format == 'fb2':
            book_text: str = parse_fb2(book_text)

        book: dict[int: str] = await BookObjectStore.upload_book(book_text, book_id, is_admin=True)
        await add_admin_book(admin_username=message.from_user.username, book_id=book_id,
                             book_title=book_title, page_count=len(book))
        await message.answer(text=LEXICON_RU['admin_book_download_end'])
        await state.clear()


@router.message(StateFilter(FSMAdminBook.admin_book_send), ~IsCorrectAdminBook())
async def not_admin_send_book_warning(message: Message):
    await message.answer(text=LEXICON_RU['other_format_admin_send_book'])