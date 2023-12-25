from config_data.config import Config
from aiomysql.utils import _PoolAcquireContextManager
from asyncio import ProactorEventLoop
from aiomysql import Pool, create_pool


async def db_connection(running_loop: ProactorEventLoop, config: Config) -> tuple[Pool, _PoolAcquireContextManager]:
    global connection
    
    pool: Pool = await create_pool(
        loop=running_loop,
        host=config.db.host,
        port=config.db.port,
        db=config.db.name,
        user=config.db.user,
        password=config.db.password,
        autocommit=True
    )

    async with pool.acquire() as connection:
        pass

    return pool, connection


async def execute_query(query: str, main_operand: str, *args: tuple) -> tuple | list[tuple]:

    async with connection.cursor() as cursor:

        await cursor.execute(query, args)

        main_operand: str = main_operand.lower()

        if main_operand == 'select_one':
            return await cursor.fetchone()
        
        if main_operand == 'select_all':
            return await cursor.fetchall()