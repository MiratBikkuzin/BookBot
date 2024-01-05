from config_data.config import load_config

from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in load_config().tg_bot.admin_ids


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