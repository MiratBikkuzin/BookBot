from keyboards.bookmarks_kb import create_bookmarks_kb, create_edit_kb
from keyboards.pagination_kb import create_pagination_kb
from lexicon.lexicon import LEXICON_RU
from db.db_queries import *
from db.methods import execute_query
from services.file_handling import book
from filters.filters import (
    IsAddBookmarkCallbackData,
    IsDigitCallbackData,
    IsDelBookmarkCallbackData
)

from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from itertools import chain


router: Router = Router(name='UserRouter')


@router.message(CommandStart())
async def process_start_command(message: Message) -> None:

    user_id: int = message.from_user.id
    firstname: str = message.from_user.first_name

    if not await execute_query(select_user_info_query, 'SELECT_ONE', user_id):
        await execute_query(add_user_info_query, 'INSERT', user_id, 0)
        await message.answer(LEXICON_RU[message.text] % firstname)

    else:
        await message.answer(LEXICON_RU['reset_start'] % firstname)


@router.message(Command(commands='help'))
async def process_help_command(message: Message) -> None:
    await message.answer(LEXICON_RU[message.text])


@router.message(Command(commands='beginning'))
async def process_beginning_command(message: Message) -> None:

    user_book_page: int = 1
    await execute_query(update_user_page_query, 'UPDATE',
                        user_book_page, message.from_user.id)

    await message.answer(
        text=book[user_book_page],
        reply_markup=create_pagination_kb()
    )


@router.message(Command(commands='continue'))
async def process_continue_command(message: Message) -> None:
    
    _, user_book_page = await execute_query(select_user_info_query, 'SELECT_ONE', message.from_user.id)

    await message.answer(
        text=book[user_book_page],
        reply_markup=create_pagination_kb(user_book_page)
    )


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
            reply_markup=create_bookmarks_kb(*user_bookmarks)
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


@router.callback_query(F.data.in_(('forward', 'backward')))
async def process_page_turning(callback: CallbackQuery) -> None:

    user_id, user_book_page = await execute_query(select_user_info_query, 'SELECT_ONE', callback.from_user.id)
    user_book_page += -1 if callback.data == 'backward' else 1

    await execute_query(update_user_page_query, 'UPDATE',
                        user_book_page, user_id)
    await callback.message.edit_text(
        text=book[user_book_page],
        reply_markup=create_pagination_kb(user_book_page)
    )


@router.callback_query(IsDigitCallbackData())
async def process_bookmark_press(callback: CallbackQuery) -> None:
    await callback.message.edit_text(book[int(callback.data)])


@router.callback_query(F.data == 'edit_bookmarks')
async def process_edit_bookmark(callback: CallbackQuery) -> None:
    
    user_bookmarks: iter[int] = chain.from_iterable(
        await execute_query(select_user_bookmarks_query,
                            'SELECT_ALL',
                            callback.from_user.id)
    )

    await callback.message.edit_text(
        text=LEXICON_RU['edit_bookmarks'],
        reply_markup=create_edit_kb(*user_bookmarks)
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
            reply_markup=create_bookmarks_kb(*user_bookmarks)
        )

    else:
        await callback.message.edit_text(LEXICON_RU['no_bookmarks'])


@router.callback_query(F.data == 'cancel')
async def process_cancel_press(callback: CallbackQuery) -> None:
    await callback.message.edit_text(LEXICON_RU['cancel_text'])