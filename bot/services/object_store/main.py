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

    nc: Client = await nats.connect(f'nats://{nats_settings.host}:{nats_settings.port}')
    js: JetStreamContext = nc.jetstream()
    
    try:
        object_store = await js.object_store(nats_settings.bucket)

    except BucketNotFoundError:
        object_store = await js.create_object_store(nats_settings.bucket)

    return object_store


def _get_book_page_key(book_id: str, page_num: int) -> str:
    return book_id + '/' + str(page_num)


class BookObjectStore:

    @staticmethod
    async def upload_book(book_text: str, book_id: str) -> dict[int: str] | None:

        book: dict[int: str] = prepare_book(book_text)

        for page_num, content in book.items():
            key: str = _get_book_page_key(book_id, page_num)
            await object_store.put(name=key, data=content)

        return book
    
    @staticmethod   
    async def get_book_page_content(book_id: str, page_num: int) -> str:
        key: str = _get_book_page_key(book_id, page_num)
        obr = await object_store.get(key)
        return obr.data.decode()
    
    @staticmethod
    async def del_book(book_id: str, book_page_count: int) -> None:
        for page_num in range(1, book_page_count + 1):
            key: str = _get_book_page_key(book_id, page_num)
            await object_store.delete(key)