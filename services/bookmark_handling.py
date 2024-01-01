from db.db_queries import select_user_bookmarks_query
from db.methods import execute_query

from itertools import chain


async def get_user_bookmarks(user_id: int) -> tuple[int]:
    return tuple(chain.from_iterable(await execute_query(
        select_user_bookmarks_query,
        'SELECT_ALL',
        user_id)
    ))