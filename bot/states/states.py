from aiogram.fsm.state import State, StatesGroup


class FSMAdminBook(StatesGroup):
    admin_book_send = State()


class FSMUserBook(StatesGroup):
    send_book_author = State()
    send_book_name = State()
    send_book_file = State()