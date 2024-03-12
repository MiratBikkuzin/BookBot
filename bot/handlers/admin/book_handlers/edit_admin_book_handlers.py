from filters.filters import IsAdmin
from keyboards.books_kb import BooksKeyboard
from keyboards.kb_utils import EditAdminBookCallbackFactory
from database.methods.delete import del_admin_book
from database.methods.get import get_admin_book_info
from services.object_store.main import BookObjectStore
from lexicon.lexicon import LEXICON_RU

from aiogram import Router, F
from aiogram.types import CallbackQuery


router: Router = Router(name=__name__)


@router.callback_query(F.data == 'admin-edit-books', IsAdmin())
async def process_edit_admin_books(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['admin_edit_books'],
        reply_markup=await BooksKeyboard.create_edit_admin_books_kb()
    )


@router.callback_query(EditAdminBookCallbackFactory.filter(), IsAdmin())
async def process_delete_admin_book(callback: CallbackQuery,
                                    callback_data: EditAdminBookCallbackFactory):
    
    admin_username: str = callback.from_user.username
    book_id: str = callback_data.book_id
    _, book_page_count = await get_admin_book_info(book_id)

    await del_admin_book(admin_username, book_id)
    await BookObjectStore.del_book(book_id, book_page_count)

    await callback.answer(text=LEXICON_RU['admin_del_book_end'])
    await callback.message.edit_text(
        text=LEXICON_RU['/update'],
        reply_markup=BooksKeyboard.create_selecting_admin_actions_kb()
    )


@router.callback_query(F.data == 'back-from-edit-admin-books', IsAdmin())
async def process_back_from_edit_admin_books_list(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['/update'],
        reply_markup=BooksKeyboard.create_selecting_admin_actions_kb()
    )