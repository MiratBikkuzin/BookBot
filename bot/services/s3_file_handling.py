import re
import json

from config_data.config import s3_settings
from services.book_text_handling import prepare_book

from typing import BinaryIO
from types_aiobotocore_s3.client import S3Client


def _get_s3_book_key(book_id: str, user_id: int, is_admin: bool = False) -> str:
    if is_admin:
        return f'admin/{book_id}.json'
    return f'user/{user_id}/{book_id}.json'


async def upload_book_s3(binary_book: BinaryIO, book_id: str,
                         user_id: int, is_admin: bool = False) -> bool:

    with binary_book:
        book_text: str = binary_book.read().decode('utf-8').replace('\n\n', '\n')
        book_text: str = re.sub(r'\n(?!    )', ' ', book_text)

    book: dict[int: str] = prepare_book(book_text)

    async with s3_settings.client as s3:
        s3: S3Client
        key: str = _get_s3_book_key(book_id, user_id, is_admin)
        await s3.put_object(Bucket=s3_settings.bucket_name, Key=key, Body=json.dumps(book))

    return True


async def get_book_s3(book_id: str, user_id: int, is_admin: bool = False) -> dict[int: str]:

    async with s3_settings.client as s3:
        s3: S3Client

        key: str = _get_s3_book_key(book_id, user_id, is_admin)
        book_obj = await s3.get_object(Bucket=s3_settings.bucket_name, Key=key)

        async with book_obj['Body'] as stream:
            return json.loads(await stream.read())
        

async def delete_book_s3(book_id: str, user_id: int, is_admin: bool = False) -> bool:
    async with s3_settings.client as s3:
        s3: S3Client
        key: str = _get_s3_book_key(book_id, user_id, is_admin)
        await s3.delete_object(Bucket=s3_settings.bucket_name, Key=key)