import re
import json

from config_data.config import settings
from services.book_text_handling import prepare_book

from typing import BinaryIO
from types_aiobotocore_s3.client import S3Client


async def upload_book_s3(binary_book: BinaryIO, book_title: str,
                         user_tg_id: int, is_admin: bool = False) -> bool:

    s3_obj_key: str = f'{user_tg_id}/{book_title}'

    if is_admin:
        s3_obj_key: str = f'admin/{user_tg_id}/{book_title}'

    with binary_book:
        book_text: str = binary_book.read().decode('utf-8').replace('\n\n', '\n')
        book_text: str = re.sub(r'\n(?!    )', ' ', book_text)

    book: dict[int: str] = prepare_book(book_text)

    async with settings.s3_client as s3:
        s3: S3Client
        await s3.put_object(Bucket=settings.s3_bucket, Key=s3_obj_key, Body=json.dumps(book))

    return True