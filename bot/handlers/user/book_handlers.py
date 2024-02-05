from lexicon.lexicon import LEXICON_RU
from keyboards.books_kb import BooksKeyboard
from keyboards.kb_utils import AdminBookCallbackFactory, UserBookCallbackFactory
from keyboards.pagination_kb import create_pagination_kb
from services.s3_file_handling import get_book_s3
from database.methods.get import get_admin_book_info, get_user_book_info
from database.methods.create import add_user_book

from aiogram import Router, F
from aiogram.filters import Command, or_f
from aiogram.types import Message, CallbackQuery


router: Router = Router(name=__name__)


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

    book: dict[str: str] = await get_book_s3(book_id, user_id, is_admin=True)

    if not user_book_info:
        current_page_num: int = 1
        await add_user_book(user_id=user_id, book_id=book_id, book_title=book_title,
                            page_count=page_count, is_admin_book=True)
        
    else:
        current_page_num: int = user_book_info[2]

    await callback.message.answer(
        text=book[str(current_page_num)],
        reply_markup=create_pagination_kb(page_count=page_count,
                                          page=current_page_num)
    )


@router.callback_query(UserBookCallbackFactory.filter())
async def process_user_book_choice(callback: CallbackQuery,
                                   callback_data: UserBookCallbackFactory) -> None:

    user_id, book_id = callback.from_user.id, callback_data.book_id
    _, page_count, current_page_num, is_admin = await get_user_book_info(user_id, book_id)

    book: dict[str: str] = await get_book_s3(book_id, user_id, is_admin)

    await callback.message.answer(
        text=book[str(current_page_num)],
        reply_markup=create_pagination_kb(page_count, current_page_num)
    )


@router.message(Command(commands='continue'))
async def process_continue_command(message: Message) -> None:
    await message.answer(
        text=LEXICON_RU['user_books_list'],
        reply_markup=await BooksKeyboard.get_user_books_kb(message.from_user.id)
    )



# @router.callback_query(F.data.in_(('forward', 'backward')))
# async def process_page_turning(callback: CallbackQuery) -> None:

#     user_id, user_book_page = await get_user_info(user_id=callback.from_user.id)
#     user_book_page += -1 if callback.data == 'backward' else 1

#     await update_user_page(new_page=user_book_page, user_id=user_id)
    
#     await callback.message.edit_text(
#         text=book[user_book_page],
#         reply_markup=create_pagination_kb(user_book_page)
#     )