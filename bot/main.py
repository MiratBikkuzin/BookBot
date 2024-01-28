import asyncio
import logging

from config_data.config import settings
from database.models import register_models
from handlers import (start_handlers, book_handlers, bookmark_handlers,
                      admin_book_handlers, other_handlers)
from keyboards.main_menu import set_main_menu

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


logger = logging.getLogger(__name__)


async def start_bot() -> None:

    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')

    bot: Bot = Bot(token=settings.bot_token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=MemoryStorage())

    dp.include_routers(
        start_handlers.router,
        book_handlers.router,
        bookmark_handlers.router,
        admin_book_handlers.router,
        other_handlers.router
    )

    await set_main_menu(bot)
    await register_models()
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start_bot())