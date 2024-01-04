import io
import re


PAGE_SIZE: int = 1100


book: dict[str: dict[int: str]] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    edit_text: str = re.sub(r'[.,!?:;]\.*$', '...', text[start:start + size])
    edit_text: str = re.findall(r'(?s).+[.,!?:;]', edit_text)
    edit_text: str = edit_text[0].strip()
    return edit_text, len(edit_text)


def prepare_book(path: io.BytesIO, book_name: str) -> None:

    book_text: str = path.read().decode('utf-8').replace('\n\n', '\n')
    book[book_name] = {}

    start, page_num = 0, 1

    while start < len(book_text):
        part_text, part_size = _get_part_text(book_text, start, PAGE_SIZE)
        book[book_name][page_num] = part_text
        start += part_size + 1
        page_num += 1