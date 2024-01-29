from database.methods.create import add_user_bookmark
from database.methods.delete import del_user_bookmark
from filters.filters import (
    IsAddBookmarkCallbackData,
    IsDigitCallbackData,
    IsDelBookmarkCallbackData
)
from services.file_handling import book
from services.bookmark_handling import get_user_bookmarks_tuple
from lexicon.lexicon import LEXICON_RU
from keyboards.bookmarks_kb import BookmarkFactory

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery


router: Router = Router(name=__name__)


@router.message(Command(commands='bookmarks'))
async def process_bookmarks_command(message: Message) -> None:

    user_id: int = message.from_user.id

    if await get_user_bookmarks_tuple(user_id=user_id):
        await message.answer(
            text=LEXICON_RU[message.text],
            reply_markup=BookmarkFactory.create_bookmarks_kb(await get_user_bookmarks_tuple(user_id=user_id))
        )

    else:
        await message.answer(LEXICON_RU['no_bookmarks'])


@router.callback_query(IsAddBookmarkCallbackData())
async def process_add_bookmark(callback: CallbackQuery, bookmark_page: int) -> None:

    user_id: int = callback.from_user.id

    if bookmark_page not in await get_user_bookmarks_tuple(user_id=user_id):
        await add_user_bookmark(user_id=user_id, bookmark_page=bookmark_page)
        await callback.answer('Страница добавлена в закладки!')

    else:
        await callback.answer(
            text='Страница уже есть в ваших закладках',
            show_alert=True
        )


@router.callback_query(IsDigitCallbackData())
async def process_bookmark_press(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        text=book[int(callback.data)],
        reply_markup=BookmarkFactory.back_from_bookmark_kb()
    )


@router.callback_query(F.data == 'back_bookmark')
async def process_back_bookmark_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['/bookmarks'],
        reply_markup=BookmarkFactory.create_bookmarks_kb(await get_user_bookmarks_tuple(user_id=callback.from_user.id))
    )
    

@router.callback_query(F.data == 'edit_bookmarks')
async def process_edit_bookmark(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        text=LEXICON_RU['edit_bookmarks'],
        reply_markup=BookmarkFactory.create_edit_kb(await get_user_bookmarks_tuple(user_id=callback.from_user.id))
    )


@router.callback_query(IsDelBookmarkCallbackData())
async def process_del_bookmark_press(callback: CallbackQuery, del_bookmark_page: int) -> None:

    user_id: int = callback.from_user.id
    
    await del_user_bookmark(user_id=user_id, bookmark_page=del_bookmark_page)

    user_bookmarks: tuple[int] = await get_user_bookmarks_tuple(user_id=user_id)

    if user_bookmarks:
        await callback.message.edit_text(
            text=LEXICON_RU['/bookmarks'],
            reply_markup=BookmarkFactory.create_bookmarks_kb(user_bookmarks)
        )

    else:
        await callback.message.edit_text(LEXICON_RU['no_bookmarks'])