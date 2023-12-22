import os, sys, re


BOOK_PATH: str = 'book/book.txt'
PAGE_SIZE: int = 1100


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    edit_text: str = re.sub(r'[.,!?:;]\.*$', '...', text[start:start + size])
    edit_text: str = re.findall(r'(?s).+[.,!?:;]', edit_text)
    edit_text: str = re.sub(r'\n(?!    )', ' ', edit_text[0])  # removes unnecessary \n 
    return edit_text, len(edit_text)


def prepare_book(path: str) -> None:
    pass