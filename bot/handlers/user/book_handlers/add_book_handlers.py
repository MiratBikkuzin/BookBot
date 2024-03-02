from database.methods.create import add_user_book
from database.methods.get import get_user_book_info
from states.states import FSMUserBook, default_state
from filters.filters import IsCorrectBook
from keyboards.books_kb import BooksKeyboard
from services.object_store import BookObjectStore
from services.file_handling import parse_fb2, get_book_text
from lexicon.lexicon import LEXICON_RU
from utils.utils import get_book_id

from aiogram import Router, Bot, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext


router: Router = Router(name=__name__)


@router.message(Command(commands='add_book'), StateFilter(default_state))
async def process_add_book_command(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU[message.text],
                         reply_markup=BooksKeyboard.get_cancel_add_book_kb())
    await state.set_state(FSMUserBook.user_book_send)


@router.callback_query(F.data == 'cancel_add_book', ~StateFilter(default_state))
async def cancel_add_book_process(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer(
        text=LEXICON_RU['cancel_add_book_end'],
        reply_markup=BooksKeyboard.create_choice_books_kb()
    )
    await callback.answer()


@router.message(StateFilter(FSMUserBook.user_book_send), IsCorrectBook())
async def process_user_send_book(message: Message, bot: Bot, book_file_id: str,
                                 book_title: str, file_format: str, state: FSMContext):
    
    user_id: int = message.from_user.id
    book_id: str = get_book_id(book_title.lower())

    if await get_user_book_info(user_id, book_id):
        await message.answer(text=LEXICON_RU['users_book_in_stock_warning'])

    else:

        await message.answer(text=LEXICON_RU['wait_user_book_download'])

        book_text: str = get_book_text(await bot.download(book_file_id))

        if file_format == 'fb2':
            book_text: str = parse_fb2(book_text)

        book: dict[int: str] = await BookObjectStore.upload_book(book_text, book_id)
        await add_user_book(user_id, book_id, book_title, page_count=len(book))
        await message.answer(text=LEXICON_RU['user_book_download_end'])
        await state.clear()


@router.message(StateFilter(FSMUserBook.user_book_send), ~IsCorrectBook())
async def not_user_send_book_warning(message: Message):
    await message.answer(
        text=LEXICON_RU['other_format_send_book'],
        reply_markup=BooksKeyboard.get_cancel_add_book_kb()
    )