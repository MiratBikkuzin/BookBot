from keyboards.books_kb import BooksKeyboard
from keyboards.kb_utils import EditAdminBookCallbackFactory
from database.methods.delete import del_admin_book
from lexicon.lexicon import LEXICON_RU

from aiogram import Router, F
from aiogram.types import CallbackQuery


router: Router = Router(name=__name__)


@router.callback_query(F.data == 'edit-admin-books')
async def process_edit_admin_books(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['edit_admin_books'],
        reply_markup=BooksKeyboard.create_edit_admin_books_kb()
    )