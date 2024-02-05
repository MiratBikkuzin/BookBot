from bs4 import BeautifulSoup as BS


def parse_fb2(fb2_doc: str) -> str:
    soup: BS = BS(fb2_doc, 'lxml')
    return soup.get_text(separator='\n', strip=True)