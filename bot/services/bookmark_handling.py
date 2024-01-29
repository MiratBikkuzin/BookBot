from database.methods.get import get_user_bookmarks

from itertools import chain


async def get_user_bookmarks_tuple(user_id: int) -> tuple[int]:
    return tuple(chain.from_iterable(await get_user_bookmarks(user_id)))