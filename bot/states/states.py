from aiogram.fsm.state import default_state, State, StatesGroup


class FSMAdminBook(StatesGroup):
    admin_book_send = State()


class FSMUserBook(StatesGroup):
    user_book_send = State()