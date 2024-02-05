import re


PAGE_SIZE: int = 1100


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int] | tuple[None, None]:
    edit_text: str = re.sub(r'[.,!?:;]\.*$', '...', text[start:start + size])
    edit_text: str = re.findall(r'(?s).+[.,!?:;]', edit_text)
    if edit_text:
        edit_text: str = edit_text[0].strip()
        return edit_text, len(edit_text)
    return None, None


def prepare_book(book_text: str) -> dict[int: str]:

    book: dict[int: str] = {}

    start, page_num = 0, 1

    while start < len(book_text):
        part_text, part_size = _get_part_text(book_text, start, PAGE_SIZE)
        if (part_text, part_size) == (None, None):
            break
        book[page_num] = part_text
        start += part_size + 1
        page_num += 1

    return book