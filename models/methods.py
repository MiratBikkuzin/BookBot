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
        password=config.db.password
    )

    async with pool.acquire() as connection:
        pass

    return pool, connection