from database.methods.create import add_admin_book
from filters.filters import IsAdmin, IsCorrectAdminBook
from states.states import FSMAdminBook, default_state
from services.s3_file_handling import upload_book_s3, get_book_s3
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
async def admin_send_book(message: Message, bot: Bot, book_file_id: str,
                          book_title: str, state: FSMContext):
    
    await message.answer(text=LEXICON_RU['wait_admin_book_download'])
    user_id: int = message.from_user.id
    book_id: str = get_book_id(book_title)

    try:
        book: dict[int: str] = await get_book_s3(book_id, user_id, is_admin=True)

    except:
        book: None = None
    
    if not book:
        book: dict[int: str] = await upload_book_s3(binary_book=await bot.download(book_file_id),
                                                    book_id=book_id, user_id=user_id,
                                                    is_admin=True)
        await add_admin_book(admin_username=message.from_user.username, book_id=book_id,
                             book_title=book_title, page_count=len(book))
        await message.answer(text=LEXICON_RU['admin_book_download_end'])
        await state.clear()

    else:
        await message.answer(text=LEXICON_RU['admins_book_in_stock_warning'])


@router.message(StateFilter(FSMAdminBook.admin_book_send), ~IsCorrectAdminBook())
async def not_admin_send_book_warning(message: Message):
    await message.answer(text=LEXICON_RU['other_format_admin_send_book'])