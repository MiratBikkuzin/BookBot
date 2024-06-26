import asyncio
import logging

from config_data.config import bot_settings
from database.models import register_models
from handlers import (read_book_handlers, bookmark_handlers, info_handlers, edit_book_handlers,
                      add_book_handlers, start_handlers, pay_handlers, start_admin_handlers,
                      add_admin_book_handlers, edit_admin_book_handlers, other_handlers)
from keyboards.main_menu import set_main_menu
from services.object_store.main import register_object_store
from utils.aiohttp_utils import AiohttpSingleton

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
        add_book_handlers.router,
        pay_handlers.router,
        info_handlers.router,
        edit_book_handlers.router,
        start_handlers.router,
        add_admin_book_handlers.router,
        edit_admin_book_handlers.router,
        start_admin_handlers.router,
        other_handlers.router
    )

    await set_main_menu(bot)
    await register_models()
    await register_object_store()
    await AiohttpSingleton()
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    await AiohttpSingleton.session.close()


if __name__ == '__main__':
    asyncio.run(start_bot())