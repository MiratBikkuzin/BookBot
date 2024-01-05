from aiogram.fsm.state import default_state, State, StatesGroup


class FSMAdminBook(StatesGroup):
    admin_book_title = State()
    admin_book_document = State()


class FSMUserBook(StatesGroup):
    user_book_title = State()
    user_book_document = State()