from services.object_store.main import object_store
from services.book_text_handling import prepare_book


class ObjectStoreHelper:

    def __get_book_page_key(self, book_id: str, page_num: int, is_admin: bool = False) -> str:
        general_key: str = book_id + '/' + str(page_num)
        if is_admin:
            return 'admin/' + general_key
        return 'user/' + general_key