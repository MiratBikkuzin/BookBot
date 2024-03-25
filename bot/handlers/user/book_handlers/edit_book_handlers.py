from keyboards.books_kb import BooksKeyboard
from keyboards.kb_utils import EditUserBookCallbackFactory
from database.methods.delete import del_user_book
from database.methods.get import get_user_book_info, get_num_readers_book, get_user_books
from services.object_store.main import BookObjectStore
from lexicon.lexicon import LEXICON_RU

from aiogram import Router, F
from aiogram.types import CallbackQuery


router: Router = Router(name=__name__)


@router.callback_query(F.data == 'edit-user-books')
async def process_edit_user_books_button_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['edit_user_books'],
        reply_markup=await BooksKeyboard.create_edit_user_books_kb(callback.from_user.id)
    )


@router.callback_query(EditUserBookCallbackFactory.filter())
async def process_del_user_book(callback: CallbackQuery,
                                callback_data: EditUserBookCallbackFactory):
    
    user_id: int = callback.from_user.id
    book_id: str = callback_data.book_id
    _, book_title, page_count, _, is_admin_book = await get_user_book_info(user_id, book_id)

    if not is_admin_book and await get_num_readers_book(book_id) <= 1:
        await BookObjectStore.del_book(book_id, page_count)

    await del_user_book(user_id, book_id)

    user_books: list[tuple[str, str, str, int]] = await get_user_books(user_id)

    await callback.answer(text=LEXICON_RU['del_user_book_end'] % book_title)

    if user_books:
        await callback.message.edit_text(
            text=LEXICON_RU['edit_user_books'],
            reply_markup=await BooksKeyboard.create_edit_user_books_kb(user_id, user_books)
        )

    else:
        await callback.message.edit_text(text=LEXICON_RU['no_books_warning'])