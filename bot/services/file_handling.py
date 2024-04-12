from io import BytesIO
from bs4 import BeautifulSoup as BS
from pypdf import PdfReader
import chardet


def get_book_text(binary_book: BytesIO) -> str:
    with binary_book:
        byte_text: bytes = binary_book.read()
        encoding: str = chardet.detect(byte_text)['encoding']
        return byte_text.decode(encoding)


def parse_fb2(fb2_doc: str) -> str:
    soup: BS = BS(fb2_doc, 'lxml')
    return soup.get_text(separator='\n', strip=True)


async def parse_pdf(pdf_doc: str) -> str:

    reader = PdfReader(stream=pdf_doc)
    all_pages_content: str = ''

    for page in reader.pages:
        all_pages_content += page.extract_text()
        
    return all_pages_content