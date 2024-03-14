from config_data.config import bot_settings

from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in bot_settings.admin_ids_lst
    

class IsCorrectBookFormat(BaseFilter):
    async def __call__(self, message: Message) -> bool | None:
        file_format: str = message.document.file_name.split('.')[-1]
        if file_format in ('fb2', 'txt'):
            return {'book_file_id': message.document.file_id, 'file_format': file_format}