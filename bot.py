import asyncio
import logging

from config_data.config import Config, load_config
from db.methods import db_connection
from handlers.user_handlers import (start_handlers, book_handlers,
                                    bookmark_handlers, other_handlers)
from keyboards.main_menu import set_main_menu

from aiogram import Bot, Dispatcher


logger = logging.getLogger(__name__)


async def main() -> None:

    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')

    config: Config = load_config()
    bot: Bot = Bot(token=config.tg_bot.bot_token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    await set_main_menu(bot)

    dp.include_routers(
        start_handlers.router,
        book_handlers.router,
        bookmark_handlers.router,
        other_handlers.router
    )

    pool, connection = await db_connection(running_loop=asyncio.get_running_loop(),
                                           config=config)
    
    async with connection:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

    pool.close()
    await pool.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())