from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class IsAddBookmarkCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        callback_data: str = callback.data
        if '/' in callback_data and callback_data.replace('/', '', 1).isdigit():
            return {'bookmark_page': int(callback_data.split('/')[0])}


class IsDigitCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data.isdigit()
    

class IsDelBookmarkCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data.endswith('del') and callback.data[:-3].isdigit()