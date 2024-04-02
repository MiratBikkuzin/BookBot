from config_data.config import merchant_settings
from urllib import parse
import hashlib


def _calculate_signature(*args) -> str:
    '''Create MD5 signature'''
    return hashlib.md5(':'.join(str(arg) for arg in args).encode()).hexdigest()


def generate_payment_link(
        user_id: int,
        num_books_to_add: int | str,
        price: int, # Cost of goods, RU
        description: str, # Description of the purchase
        inv_id: int = 0,
        price_curr: str = 'RUB',
        is_test: int = 0,
        robokassa_payment_url: str = 'https://auth.robokassa.ru/Merchant/Index.aspx'
) -> str:
    
    login: str = merchant_settings.login
    password_1: str = merchant_settings.password_1
    shp_numbooks: str = f'Shp_numbooks={num_books_to_add}'
    shp_userid: str = f'Shp_userid={user_id}'
    shp_params: list[str, str] = sorted((shp_numbooks, shp_userid))

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