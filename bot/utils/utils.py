import hashlib
from lexicon.lexicon import LEXICON_RU, PROFILE_LEXICON_RU


def get_book_id(book_author: str, book_name: str) -> str:
    hash_obj = hashlib.sha1(bytes(f'{book_name} ({book_author})', 'utf-8'))
    return hash_obj.hexdigest()


def get_profile_command_text(name: str, user_id: int, books_num: int,
                             num_books_to_add: int | str, bookmarks_num: int) -> str:
    
    if isinstance(num_books_to_add, str):
        num_books_to_add: str = LEXICON_RU['unlimited']

    return f"{PROFILE_LEXICON_RU['profile']}\n\n" \
           f"{PROFILE_LEXICON_RU['name']} {name}\n" \
           f"{PROFILE_LEXICON_RU['id']} {user_id}\n\n" \
           f"{PROFILE_LEXICON_RU['books_started']} {books_num}\n" \
           f"{PROFILE_LEXICON_RU['remaining_additions']} {num_books_to_add}\n" \
           f"{PROFILE_LEXICON_RU['bookmarks_number']} {bookmarks_num}"