from keyboards.books_kb import BooksKeyboard
from keyboards.kb_utils import EditUserBookCallbackFactory
from database.methods.delete import del_user_book
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