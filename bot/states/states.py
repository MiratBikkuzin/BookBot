from aiogram.fsm.state import State, StatesGroup


class FSMAdminBook(StatesGroup):
    admin_book_send = State()


class FSMUserBook(StatesGroup):
    user_book_send = State()