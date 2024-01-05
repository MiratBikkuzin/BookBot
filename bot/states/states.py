from aiogram.fsm.state import default_state, State, StatesGroup


class FSMAdminBook(StatesGroup):
    admin_book_document = State()
    admin_book_name = State()


class FSMUserBook(StatesGroup):
    user_book_document = State()
    user_book_name = State()