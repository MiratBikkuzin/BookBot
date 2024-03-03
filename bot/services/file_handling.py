from io import BytesIO
from bs4 import BeautifulSoup as BS
import chardet


def get_book_text(binary_book: BytesIO) -> str:
    with binary_book:
        byte_text: bytes = binary_book.read()
        encoding: str = chardet.detect(byte_text)['encoding']
        return byte_text.decode(encoding).replace('\n\n', '\n')


def parse_fb2(fb2_doc: str) -> str:
    soup: BS = BS(fb2_doc, 'lxml')
    return soup.get_text(separator='\n', strip=True)