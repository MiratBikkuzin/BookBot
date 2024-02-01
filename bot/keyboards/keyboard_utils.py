from aiogram.filters.callback_data import CallbackData


class AdminBooksCallbackFactory(CallbackData, prefix='admin-books'):
    total_page_count: int
    book_title: str


class UserBooksCallbackFactory(CallbackData, prefix='user-books'):
    total_page_count: int
    book_title: str


class BookmarksCallbackFactory(CallbackData, prefix='bookmarks'):
    page_number: int
    book_title: str


class DelBookmarksCallbackFacotry(CallbackData, prefix='del-bookmarks'):
    page_number: int
    book_title: str