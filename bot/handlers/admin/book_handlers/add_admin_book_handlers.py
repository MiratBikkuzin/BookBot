from database.methods.create import add_admin_book
from database.methods.get import get_admin_book_info
from filters.filters import IsCorrectBook
from states.states import FSMAdminBook
from keyboards.books_kb import BooksKeyboard
from services.object_store import BookObjectStore
from services.file_handling import parse_fb2, get_book_text
from lexicon.lexicon import LEXICON_RU
from utils.utils import get_book_id

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext


router: Router = Router(name=__name__)


@router.callback_query(F.data == 'admin-add-book', StateFilter(default_state))
async def admin_selecting_add_book_action(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=LEXICON_RU['admin_add_book'])
    await state.set_state(FSMAdminBook.admin_book_send)


@router.message(StateFilter(FSMAdminBook.admin_book_send), IsCorrectBook())
async def admin_send_book(message: Message, bot: Bot, book_file_id: str, book_title: str,
                          file_format: str, state: FSMContext):
    
    book_id: str = get_book_id(book_title.lower())

    if await get_admin_book_info(book_id):
        await message.answer(text=LEXICON_RU['admins_book_in_stock_warning'])

    else:

        await message.answer(text=LEXICON_RU['wait_admin_book_download'])

        book_text: str = get_book_text(await bot.download(book_file_id))

        if file_format == 'fb2':
            book_text: str = parse_fb2(book_text)

        book: dict[int: str] = await BookObjectStore.upload_book(book_text, book_id)
        await add_admin_book(admin_username=message.from_user.username, book_id=book_id,
                             book_title=book_title, page_count=len(book))
        await message.answer(text=LEXICON_RU['admin_book_download_end'])
        await state.clear()


@router.message(StateFilter(FSMAdminBook.admin_book_send), ~IsCorrectBook())
async def not_admin_send_book_warning(message: Message):
    await message.answer(
        text=LEXICON_RU['other_format_send_book'],
        reply_markup=BooksKeyboard.create_cancel_add_book_kb()
    )