import decimal
import hashlib
from urllib import parse
from urllib.parse import urlparse


def _calculate_signature(*args) -> str:
    '''Create MD5 signature'''
    return hashlib.md5(':'.join(str(arg) for arg in args).encode()).hexdigest()


