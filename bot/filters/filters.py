from config_data.config import bot_settings

from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in bot_settings.admin_ids_lst
    

class IsCorrectAdminBook(BaseFilter):
    async def __call__(self, message: Message) -> bool | None:
        if message.document and message.caption:
            if message.document.file_name.split('.')[-1] in ('fb2', 'txt'):
                return {'book_file_id': message.document.file_id, 'book_title': message.caption}


class IsAddBookmarkCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> dict[str: int] | None:
        callback_data: str = callback.data
        if '/' in callback_data and callback_data.replace('/', '', 1).isdigit():
            return {'bookmark_page': int(callback_data.split('/')[0])}


class IsDigitCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data.isdigit()
    

class IsDelBookmarkCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> dict[str: int] | None:
        callback_data: str = callback.data
        if callback_data.endswith('del') and callback_data[:-3].isdigit():
            return {'del_bookmark_page': int(callback_data[:-3])}