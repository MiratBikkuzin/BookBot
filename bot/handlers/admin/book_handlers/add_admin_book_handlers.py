from database.methods.create import add_admin_book
from database.methods.get import get_admin_book_info
from filters.filters import IsCorrectBookFormat
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
    await state.set_state(FSMAdminBook.send_book_author)
    await callback.message.answer(
        text=LEXICON_RU['admin_add_book'],
        reply_markup=BooksKeyboard.create_cancel_add_book_kb()
    )
    await callback.answer()


@router.message(StateFilter(FSMAdminBook.send_book_author))
async def process_admin_send_book_author(message: Message, state: FSMContext):
    await state.update_data(book_author=message.text)
    await state.set_state(FSMAdminBook.send_book_title)
    await message.answer(
        text=LEXICON_RU['book_name_send'],
        reply_markup=BooksKeyboard.create_cancel_add_book_kb()
    )


@router.message(StateFilter(FSMAdminBook.send_book_title))
async def process_admin_send_book_name(message: Message, state: FSMContext):
    await state.update_data(book_title=message.text)
    await state.set_state(FSMAdminBook.send_book_file)
    await message.answer(
        text=LEXICON_RU['book_file_send'],
        reply_markup=BooksKeyboard.create_cancel_add_book_kb()
    )


@router.message(StateFilter(FSMAdminBook.send_book_file), IsCorrectBookFormat())
async def process_admin_send_book_file(message: Message, bot: Bot, book_file_id: str,
                                       file_format: str, state: FSMContext):
    
    data: dict[str: str, str: str] = await state.get_data()
    book_author, book_title = data['book_author'], data['book_title']
    book_id: str = get_book_id(book_author, book_title)

    if await get_admin_book_info(book_id):
        await message.answer(text=LEXICON_RU['admins_book_in_stock_warning'])

    else:

        await message.answer(text=LEXICON_RU['wait_admin_book_download'])

        book_text: str = get_book_text(await bot.download(book_file_id))

        if file_format == 'fb2':
            book_text: str = parse_fb2(book_text)

        book: dict[int: str] = await BookObjectStore.upload_book(book_text, book_id)
        await add_admin_book(admin_username=message.from_user.username, book_id=book_id,
                             book_author=book_author, book_title=book_title, page_count=len(book))
        await message.answer(text=LEXICON_RU['admin_book_download_end'])
        await state.clear()


@router.message(StateFilter(FSMAdminBook.send_book_file), ~IsCorrectBookFormat())
async def not_admin_send_book_file_warning(message: Message):
    await message.answer(
        text=LEXICON_RU['other_format_send_book'],
        reply_markup=BooksKeyboard.create_cancel_add_book_kb()
    )