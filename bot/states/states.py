from aiogram.fsm.state import State, StatesGroup


class FSMAdminBook(StatesGroup):
    admin_book_send = State()


class FSMUserBook(StatesGroup):
    book_author_send = State()
    book_file_send = State()