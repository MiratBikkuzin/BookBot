import re
from typing import BinaryIO


PAGE_SIZE: int = 1100


book: dict[str: dict[int: str]] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int] | tuple[None, None]:
    edit_text: str = re.sub(r'[.,!?:;]\.*$', '...', text[start:start + size])
    edit_text: str = re.findall(r'(?s).+[.,!?:;]', edit_text)
    if edit_text:
        edit_text: str = edit_text[0].strip()
        return edit_text, len(edit_text)
    return None, None


def prepare_book(binary_book: BinaryIO, book_title: str) -> bool | None:

    if book_title.lower() not in map(str.lower, book.keys()):

        book[book_title] = {}

        with binary_book:
            book_text: str = binary_book.read().decode('utf-8').replace('\n\n', '\n')
            book_text: str = re.sub(r'\n(?!    )', ' ', book_text)

        start, page_num = 0, 1

        while start < len(book_text):
            part_text, part_size = _get_part_text(book_text, start, PAGE_SIZE)
            if (part_text, part_size) == (None, None):
                break
            book[book_title][page_num] = part_text
            start += part_size + 1
            page_num += 1

        return True