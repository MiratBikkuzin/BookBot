from db.db_queries import add_admin_books, admin_books_query, admin_books_count_query
from db.methods import execute_query
from states.states import default_state, FSMAdminBook

from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext


router: Router = Router(name=__name__)