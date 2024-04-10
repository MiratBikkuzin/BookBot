from config_data.config import merchant_settings
from database.methods.create import add_user_payment_info
from database.methods.get import check_is_invoice_id_unique, get_user_invoice_id
from database.methods.update import update_payment_info

from urllib import parse
from random import randint
from aiohttp import ClientSession
from bs4 import BeautifulSoup as BS
import hashlib


def _calculate_signature(*args) -> str:
    '''Create MD5 signature'''
    return hashlib.md5(':'.join(str(arg) for arg in args).encode()).hexdigest()


def _generate_payment_verification_link(
        inv_id: int,
        check_payment_url = 'https://auth.robokassa.ru/Merchant/WebService/Service.asmx/OpStateExt'
) -> str:
    
    login: str = merchant_settings.login
    password_2: str = merchant_settings.password_2

    data = {
        'MerchantLogin': login,
        'InvoiceID': inv_id,
        'Signature': _calculate_signature(login, inv_id, password_2)
    }

    return f'{check_payment_url}?{parse.urlencode(data)}'


def generate_payment_link(
        user_id: int,
        num_books_to_add: int | str,
        price: int, # Cost of goods, RU
        description: str, # Description of the purchase
        inv_id: int,
        price_curr: str = 'RUB',
        is_test: int = 0,
        robokassa_payment_url: str = 'https://auth.robokassa.ru/Merchant/Index.aspx'
) -> str:
    
    login: str = merchant_settings.login
    password_1: str = merchant_settings.password_1
    shp_numbooks: str = f'Shp_numbooks={num_books_to_add}'
    shp_userid: str = f'Shp_userid={user_id}'
    shp_params: list[str, str] = shp_numbooks, shp_userid

    data = {
        'MerchantLogin': login,
        'OutSum': price,
        'InvId': inv_id,
        'Description': description,
        'Shp_numbooks': num_books_to_add,
        'Shp_userid': user_id,
        'IsTest': is_test
    }
    
    if price_curr != 'RUB':
        signature = _calculate_signature(login, price, inv_id, price_curr, password_1, *shp_params)
        data['OutSumCurrency'] = price_curr

    else:
        signature = _calculate_signature(login, price, inv_id, password_1, *shp_params)

    data['SignatureValue'] = signature
    return f'{robokassa_payment_url}?{parse.urlencode(data)}'


async def create_unique_invoice_id(user_id: int) -> int:

    is_unique = False

    while is_unique is False:
        inv_id = randint(1, 2147483646)
        if await check_is_invoice_id_unique(inv_id):
            is_unique = True

    if await get_user_invoice_id(user_id):
        await update_payment_info(user_id, inv_id)

    else:
        await add_user_payment_info(user_id, inv_id)
            
    return inv_id


async def is_payment_success(
        inv_id: int,
        aiohttp_session: ClientSession
) -> tuple[int, int] | None:

    payment_verification_link: str = _generate_payment_verification_link(inv_id)
    response = await aiohttp_session.get(payment_verification_link)
    soup: BS = BS(await response.text(), 'xml')
    result_code: int = int(soup.find('Result').find('Code').text)

    if result_code == 0 and int(soup.find('State').find('Code').text) == 100:
    
        user_fields = soup.find('UserFields')
        num_books_to_add, user_id = (int(x.text) for x in user_fields.find_all('Value'))

        return num_books_to_add, user_id