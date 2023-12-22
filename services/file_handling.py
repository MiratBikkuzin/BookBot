import os, sys, re


BOOK_PATH: str = 'book/book.txt'
PAGE_SIZE: int = 1100


book: dict[int: str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    edit_text: str = re.sub(r'[.,!?:;]\.*$', '...', text[start:start + size])
    edit_text: str = re.findall(r'(?s).+[.,!?:;]', edit_text)
    edit_text: str = edit_text[0].strip()
    return edit_text, len(edit_text)


def prepare_book(path: str) -> None:
    
    with open(path, 'rt', encoding='utf-8') as book_file:
        book_text: str = book_file.read().replace('\n\n', '\n')

    start, page_num = 0, 1

    while start < len(book_text):
        part_text, part_size = _get_part_text(book_text, start, PAGE_SIZE)
        book[page_num] = part_text
        start += part_size
        page_num += 1


prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))