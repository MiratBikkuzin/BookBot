from services.object_store.main import object_store
from services.book_text_handling import prepare_book


class BookObjectStore:

    def __get_book_page_key(self, book_id: str, page_num: int, is_admin: bool = False) -> str:
        general_key: str = book_id + '/' + str(page_num)
        if is_admin:
            return 'admin/' + general_key
        return 'user/' + general_key
    

    async def upload_book(self, book_text: str, book_id: str,
                          is_admin: bool = False) -> dict[int: str] | None:

        book: dict[int: str] = prepare_book(book_text)
        objects: iter[str] = (obj.name for obj in await object_store.list())

        for page_num, content in book.items():
            key: str = self.__get_book_page_key(book_id, page_num, is_admin)
            if key in objects:
                return
            await object_store.put(name=key, data=content)

        return book
    
    async def get_book_page_content(self, book_id: str, page_num: int, is_admin: bool = False) -> str:
        key: str = self.__get_book_page_key(book_id, page_num, is_admin)
        obr = await object_store.get(key)
        return obr.data.decode()