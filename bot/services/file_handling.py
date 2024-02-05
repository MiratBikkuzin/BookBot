from typing import BinaryIO
from bs4 import BeautifulSoup as BS


def get_book_text(binary_book: BinaryIO) -> str:
    with binary_book:
        return binary_book.read().decode('utf-8').replace('\n\n', '\n')


def parse_fb2(fb2_doc: str) -> str:
    soup: BS = BS(fb2_doc, 'lxml')
    return soup.get_text(separator='\n', strip=True)