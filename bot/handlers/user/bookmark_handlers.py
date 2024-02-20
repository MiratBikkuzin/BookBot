from database.methods.create import add_user_bookmark
from database.methods.delete import del_user_bookmark
from database.methods.get import (get_user_books_with_bookmarks,
                                  get_user_book_bookmarks,
                                  get_user_book_info)
from services.object_store import BookObjectStore
from lexicon.lexicon import LEXICON_RU
from keyboards.bookmarks_kb import BookmarksKeyboard
from keyboards.kb_utils import (PageCallbackFactory, BookMarkCallbackFactory,
                                EditBookMarkCallbackFactory, BookPageMarkCallbackFactory,
                                EditBookPageMarkCallbackFactory, BackPageMarkCallbackFactory)

from aiogram import Router, F
from aiogram.filters import Command, or_f
from aiogram.types import Message, CallbackQuery


router: Router = Router(name=__name__)


@router.message(Command(commands='bookmarks'))
async def process_bookmarks_command(message: Message) -> None:

    books: list[tuple[str, str]] = await get_user_books_with_bookmarks(message.from_user.id)

    if books:
        await message.answer(
            text=LEXICON_RU[message.text],
            reply_markup=await BookmarksKeyboard.create_bookmark_kb(books)
        )

    else:
        await message.answer(LEXICON_RU['no_bookmarks'])


@router.callback_query(PageCallbackFactory.filter())
async def process_add_bookmark(callback: CallbackQuery, callback_data: PageCallbackFactory) -> None:

    user_id: int = callback.from_user.id
    book_id, page = callback_data.book_id, callback_data.page_num
    book_title, *_ = await get_user_book_info(user_id, book_id)

    if page not in await get_user_book_bookmarks(user_id, book_id):
        await add_user_bookmark(user_id, book_id, book_title, page)
        await callback.answer('Страница добавлена в закладки!')

    else:
        await callback.answer(
            text='Страница уже есть в ваших закладках',
            show_alert=True
        )


@router.callback_query(or_f(BookMarkCallbackFactory.filter(),
                            BackPageMarkCallbackFactory.filter()))
async def process_book_with_bookmarks_press(callback: CallbackQuery,
                                            callback_data: BookMarkCallbackFactory) -> None:
    
    book_id: str = callback_data.book_id
    book_bookmarks: tuple[int] = await get_user_book_bookmarks(callback.from_user.id, book_id)
    
    await callback.message.edit_text(
        text='Выберите страницу книги',
        reply_markup=await BookmarksKeyboard.create_book_page_mark_kb(book_id, book_bookmarks)
    )


@router.callback_query(BookPageMarkCallbackFactory.filter())
async def process_book_page_mark_press(callback: CallbackQuery,
                                       callback_data: BookPageMarkCallbackFactory) -> None:
    
    book_id, page_num = callback_data.book_id, callback_data.page_number

    await callback.message.edit_text(
        text=await BookObjectStore.get_book_page_content(book_id, page_num),
        reply_markup=BookmarksKeyboard.back_from_bookmark_content_kb(book_id)
    )


@router.callback_query(F.data.in_(('edit_bookmarks', 'back_from_edit_bookmarks')))
async def process_edit_bookmarks_press(callback: CallbackQuery) -> None:

    books: list[tuple[str, str]] = await get_user_books_with_bookmarks(callback.from_user.id)

    await callback.message.edit_text(
        text=LEXICON_RU['edit_bookmarks'],
        reply_markup=await BookmarksKeyboard.create_edit_bookmark_kb(books)
    )


@router.callback_query(EditBookMarkCallbackFactory.filter())
async def process_edit_book_with_bookmarks_press(callback: CallbackQuery,
                                                 callback_data: EditBookMarkCallbackFactory) -> None:
    
    book_id: str = callback_data.book_id
    book_bookmarks: tuple[int] = await get_user_book_bookmarks(callback.from_user.id, book_id)

    await callback.message.edit_text(
        text=LEXICON_RU['edit_book_page_marks'],
        reply_markup=await BookmarksKeyboard.create_edit_book_page_mark_kb(book_id, book_bookmarks)
    )


@router.callback_query(EditBookPageMarkCallbackFactory.filter())
async def process_edit_book_page_mark_press(callback: CallbackQuery,
                                            callback_data: EditBookPageMarkCallbackFactory) -> None:
    
    user_id: int = callback.from_user.id
    book_id, page_num = callback_data.book_id, callback_data.page_number

    await del_user_bookmark(user_id, book_id, page_num)

    await callback.answer(text='Закладка удалена')

    book_bookmarks: tuple[int] | None = await get_user_book_bookmarks(user_id, book_id)

    if book_bookmarks:
        await callback.message.edit_text(
            text=LEXICON_RU['edit_book_page_marks'],
            reply_markup=await BookmarksKeyboard.create_edit_book_page_mark_kb(book_id,
                                                                               book_bookmarks)
        )

    else:

        books: list[tuple[str, str]] = await get_user_books_with_bookmarks(user_id)

        if books:
            await callback.message.edit_text(
                text=LEXICON_RU['edit_bookmarks'],
                reply_markup=await BookmarksKeyboard.create_edit_bookmark_kb(books)
            )

        else:
            await callback.message.edit_text(text=LEXICON_RU['no_bookmarks'])


@router.callback_query(F.data.in_(('cancel_edit_bookmarks', 'back_from_bookmarks')))
async def process_cancel_edit_bookmarks_press(callback: CallbackQuery) -> None:

    books: list[tuple[str, str]] = await get_user_books_with_bookmarks(callback.from_user.id)

    await callback.message.edit_text(
        text=LEXICON_RU['/bookmarks'],
        reply_markup=await BookmarksKeyboard.create_bookmark_kb(books)
    )