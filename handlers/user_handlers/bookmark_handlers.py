from db.db_queries import *
from db.methods import execute_query
from filters.filters import (
    IsAddBookmarkCallbackData,
    IsDigitCallbackData,
    IsDelBookmarkCallbackData
)
from services.file_handling import book
from lexicon.lexicon import LEXICON_RU
from keyboards.bookmarks_kb import BookmarkFactory

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from itertools import chain


router: Router = Router(name=__name__)


@router.message(Command(commands='bookmarks'))
async def process_bookmarks_command(message: Message) -> None:

    if await execute_query(select_user_bookmarks_query, 'SELECT_ONE', message.from_user.id):

        user_bookmarks: iter[int] = chain.from_iterable(
            await execute_query(select_user_bookmarks_query,
                                'SELECT_ALL',
                                message.from_user.id)
        )

        await message.answer(
            text=LEXICON_RU[message.text],
            reply_markup=BookmarkFactory.create_bookmarks_kb(*user_bookmarks)
        )

    else:
        await message.answer(LEXICON_RU['no_bookmarks'])


@router.callback_query(IsAddBookmarkCallbackData())
async def process_add_bookmark(callback: CallbackQuery, bookmark_page: int) -> None:

    user_bookmarks: iter[int] = chain.from_iterable(
        await execute_query(select_user_bookmarks_query,
                            'SELECT_ALL',
                            callback.from_user.id)
    )

    if bookmark_page not in user_bookmarks:
        await execute_query(add_user_bookmark_query, 'INSERT',
                            callback.from_user.id, bookmark_page)
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
        reply_markup=BookmarkFactory.back_from_bookmark()
    )


@router.callback_query(F.data == 'edit_bookmarks')
async def process_edit_bookmark(callback: CallbackQuery) -> None:
    
    user_bookmarks: iter[int] = chain.from_iterable(
        await execute_query(select_user_bookmarks_query,
                            'SELECT_ALL',
                            callback.from_user.id)
    )

    await callback.message.edit_text(
        text=LEXICON_RU['edit_bookmarks'],
        reply_markup=BookmarkFactory.create_edit_kb(*user_bookmarks)
    )


@router.callback_query(IsDelBookmarkCallbackData())
async def process_del_bookmark_press(callback: CallbackQuery, del_bookmark_page: int) -> None:

    user_id: int = callback.from_user.id
    
    await execute_query(del_user_bookmark_query, 'DELETE',
                        user_id, del_bookmark_page)
    
    user_bookmarks: tuple[int] = tuple(chain.from_iterable(
        await execute_query(select_user_bookmarks_query,
                            'SELECT_ALL',
                            user_id)
    ))

    if user_bookmarks:
        await callback.message.edit_text(
            text=LEXICON_RU['/bookmarks'],
            reply_markup=BookmarkFactory.create_bookmarks_kb(*user_bookmarks)
        )

    else:
        await callback.message.edit_text(LEXICON_RU['no_bookmarks'])