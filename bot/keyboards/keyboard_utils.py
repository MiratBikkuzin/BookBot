from aiogram.filters.callback_data import CallbackData


class AdminBookCallbackFactory(CallbackData, prefix='admin-book'):
    total_page_count: int
    book_title: str


class UserBookCallbackFactory(CallbackData, prefix='user-book'):
    total_page_count: int
    book_title: str


class BookmarksCallbackFactory(CallbackData, prefix='bookmark'):
    page_number: int
    book_title: str


class DelBookmarksCallbackFacotry(CallbackData, prefix='del-bookmark'):
    page_number: int
    book_title: str