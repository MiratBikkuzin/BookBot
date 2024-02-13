from config_data.config import nats_settings
from services.book_text_handling import prepare_book

from nats.aio.client import Client
from nats.js import JetStreamContext
from nats.js.errors import BucketNotFoundError
from nats.js.object_store import ObjectStore

import nats


object_store: ObjectStore


async def register_object_store() -> ObjectStore:
    global object_store

    nc: Client = await nats.connect()
    js: JetStreamContext = nc.jetstream()
    
    try:
        object_store = await js.object_store(nats_settings.bucket)

    except BucketNotFoundError:
        object_store = await js.create_object_store(nats_settings.bucket)

    return object_store


def _get_book_page_key(book_id: str, page_num: int, is_admin: bool = False) -> str:
    general_key: str = book_id + '/' + str(page_num)
    if is_admin:
        return 'admin/' + general_key
    return 'user/' + general_key


class BookObjectStore:
    
    @staticmethod
    async def check_book_in_stock(book_id: str, is_admin: bool = False) -> bool:
        key: str = _get_book_page_key(book_id, 1, is_admin)
        if key in (obj.name for obj in await object_store.list(ignore_deletes=True)):
            return True
        return False

    @staticmethod
    async def upload_book(book_text: str, book_id: str,
                          is_admin: bool = False) -> dict[int: str] | None:

        book: dict[int: str] = prepare_book(book_text)

        for page_num, content in book.items():
            key: str = _get_book_page_key(book_id, page_num, is_admin)
            await object_store.put(name=key, data=content)

        return book
    
    @staticmethod   
    async def get_book_page_content(book_id: str, page_num: int, is_admin: bool = False) -> str:
        key: str = _get_book_page_key(book_id, page_num, is_admin)
        obr = await object_store.get(key)
        return obr.data.decode()
    
    @staticmethod
    async def del_book(book_id: str, book_page_count: int, is_admin: bool = False) -> None:
        for page_num in range(1, book_page_count + 1):
            key: str = _get_book_page_key(book_id, page_num, is_admin)
            await object_store.delete(key)