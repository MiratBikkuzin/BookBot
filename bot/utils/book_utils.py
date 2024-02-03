import hashlib


def get_book_id(book_title: str) -> str:
    hash_obj = hashlib.sha1(bytes(book_title, 'utf-8'))
    return hash_obj.hexdigest()