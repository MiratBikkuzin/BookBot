from keyboards.bookmarks_kb import create_bookmarks_kb, create_edit_kb
from keyboards.pagination_kb import create_pagination_kb
from lexicon.lexicon import LEXICON_RU
from models.db_queries import *
from models.methods import execute_query
from services.file_handling import book
from filters.filters import IsDigitCallbackData, IsDelBookmarkCallbackData

from aiogram import Router, F
from aiogram.filters import (
    CommandStart, Command,
    ChatMemberUpdatedFilter,
    KICKED, MEMBER
)
from aiogram.types import (
    Message,
    CallbackQuery,
    ChatMemberUpdated
)


router: Router = Router(name='UserRouter')