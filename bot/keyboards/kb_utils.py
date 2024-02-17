from aiogram.filters.callback_data import CallbackData


class AdminBookCallbackFactory(CallbackData, prefix='adminb', sep='@'):
    total_page_count: int
    book_id: str


class UserBookCallbackFactory(CallbackData, prefix='userb', sep='@'):
    total_page_count: int
    book_id: str


class BookMarkCallbackFactory(CallbackData, prefix='bmark', sep='@'):
    book_id: str


class EditBookMarkCallbackFactory(CallbackData, prefix='ebmark', sep='@'):
    book_id: str


class BookPageMarkCallbackFactory(CallbackData, prefix='bpmark', sep='@'):
    book_id: str
    page_number: int


class EditBookPageMarkCallbackFactory(CallbackData, prefix='ebpmark', sep='@'):
    book_id: str
    page_number: int


class PageTurningCallbackFactory(CallbackData, prefix='pturn', sep='@'):
    turn_type: str
    book_id: str


class PageCallbackFactory(CallbackData, prefix='p', sep='@'):
    page_num: int
    page_count: int
    book_id: str