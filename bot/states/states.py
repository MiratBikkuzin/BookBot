from aiogram.fsm.state import State, StatesGroup


class FSMAdminBook(StatesGroup):
    send_book_author = State()
    send_book_title = State()
    send_book_file = State()


class FSMUserBook(StatesGroup):
    send_book_author = State()
    send_book_title = State()
    send_book_file = State()