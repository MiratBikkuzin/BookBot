from aiogram.filters.callback_data import CallbackData


class AdminBookCallbackFactory(CallbackData, prefix='admin-book', sep='@'):
    total_page_count: int
    book_id: str


class UserBookCallbackFactory(CallbackData, prefix='user-book', sep='@'):
    total_page_count: int
    book_id: str


class BookmarksCallbackFactory(CallbackData, prefix='bookmark', sep='@'):
    page_number: int
    book_id: str


class DelBookmarksCallbackFacotry(CallbackData, prefix='del-bkmark', sep='@'):
    page_number: int
    book_id: str