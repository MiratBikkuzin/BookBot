from lexicon.lexicon import LEXICON_RU
from keyboards.books_kb import BooksKeyboard
from keyboards.kb_utils import (AdminBookCallbackFactory, UserBookCallbackFactory,
                                PageTurningCallbackFactory)
from keyboards.pagination_kb import create_pagination_kb
from services.object_store import BookObjectStore
from database.methods.create import add_user_book
from database.methods.get import get_admin_book_info, get_user_book_info
from database.methods.update import update_book_page

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery


router: Router = Router(name=__name__)


@router.callback_query(PageTurningCallbackFactory.filter())
async def process_page_turning(callback: CallbackQuery,
                               callback_data: PageTurningCallbackFactory) -> None:

    user_id, book_id = callback.from_user.id, callback_data.book_id
    _, page_count, page_num, _ = await get_user_book_info(user_id, book_id)
    page_num += -1 if callback_data.turn_type == 'backward' else 1

    page_content: str = await BookObjectStore.get_book_page_content(book_id, page_num)
    
    await callback.message.edit_text(
        text=page_content,
        reply_markup=create_pagination_kb(book_id, page_count, page_num)
    )

    await update_book_page(user_id, book_id, new_page=page_num)


@router.message(Command(commands='beginning'))
async def process_beginning_command(message: Message) -> None:
    await message.answer(
        text=LEXICON_RU['choice_books_text'],
        reply_markup=BooksKeyboard.create_choice_books_kb()
    )


@router.callback_query(F.data == 'admin-books')
async def process_admin_books_choice(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        text=LEXICON_RU['admin_books_list'],
        reply_markup=await BooksKeyboard.get_admin_books_kb()
    )


@router.callback_query(F.data == 'user-books')
async def process_user_books_choice(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        text=LEXICON_RU['user_books_list'],
        reply_markup=await BooksKeyboard.get_user_books_kb(callback.from_user.id)
    )


@router.callback_query(AdminBookCallbackFactory.filter())
async def process_admin_book_choice(callback: CallbackQuery,
                                    callback_data: AdminBookCallbackFactory) -> None:
    
    user_id, book_id = callback.from_user.id, callback_data.book_id
    book_title, page_count = await get_admin_book_info(book_id)
    user_book_info: tuple[str, int, int, bool] | None = await get_user_book_info(user_id, book_id)

    if not user_book_info:
        page_num: int = 1
        await add_user_book(user_id=user_id, book_id=book_id, book_title=book_title,
                            page_count=page_count, is_admin_book=True)
        
    else:
        page_num: int = user_book_info[2]

    page_content: str = await BookObjectStore.get_book_page_content(book_id, page_num)

    await callback.message.answer(
        text=page_content,
        reply_markup=create_pagination_kb(book_id, page_count, page_num)
    )


@router.callback_query(UserBookCallbackFactory.filter())
async def process_user_book_choice(callback: CallbackQuery,
                                   callback_data: UserBookCallbackFactory) -> None:

    user_id, book_id = callback.from_user.id, callback_data.book_id
    _, page_count, page_num, _ = await get_user_book_info(user_id, book_id)

    page_content: str = await BookObjectStore.get_book_page_content(book_id, page_num)

    await callback.message.answer(
        text=page_content,
        reply_markup=create_pagination_kb(book_id, page_count, page_num)
    )


@router.message(Command(commands='continue'))
async def process_continue_command(message: Message) -> None:
    await message.answer(
        text=LEXICON_RU['user_books_list'],
        reply_markup=await BooksKeyboard.get_user_books_kb(message.from_user.id)
    )