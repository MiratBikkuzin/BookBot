import asyncio
import logging

from config_data.config import bot_settings
from database.models import register_models
from handlers import (read_book_handlers, bookmark_handlers, main_handlers,
                      add_book_handlers, start_handlers, pay_handlers,
                      admin_book_handlers, other_handlers)
from keyboards.main_menu import set_main_menu
from services.object_store.main import register_object_store

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

    bot: Bot = Bot(token=bot_settings.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=MemoryStorage())

    dp.include_routers(
        read_book_handlers.router,
        bookmark_handlers.router,
        main_handlers.router,
        add_book_handlers.router,
        pay_handlers.router,
        start_handlers.router,
        admin_book_handlers.router,
        other_handlers.router
    )

    await set_main_menu(bot)
    await register_models()
    await register_object_store()
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start_bot())