__author__ = "Lotanna Amaechi"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Lotanna Amaechi"
__email__ = "lotanna.camaechi@gmail.com"
__status__ = "Production"

import requests
import base64
from moneybag import settings
from django.utils import timezone
import uuid
from urllib.parse import quote
import hashlib
from random import randrange

try:
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_v1_5
except ImportError:
    import sys
    sys.path.append('/anaconda3/lib/python3.6/site-packages')
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_v1_5

client_id = settings.CLIENT_ID
secret_key = settings.CLIENT_SECRET_KEY


client_id_recurrent = settings.CLIENT_ID_RECURRENT   # recurrent client id
secret_key_recurrent = settings.CLIENT_SECRET_KEY_RECURRENT  # recurrent client secret


client_id_fund_transfer = settings.CLIENT_FUND_TRANSFER_ID # fund transfer id
secret_key_fund_transfer = settings.CLIENT_FUND_TRANSFER_SECRET_KEY # client secret key


public_modulus = settings.PUBLIC_MODULUS
public_exponent = settings.PUBLIC_EXPONENT

entity_code = settings.INITIATING_ENTITY_CODE
prefix_code = settings.TRANSFER_PREFIX_CODE
terminal_id = settings.TERMINAL_ID
currency_code = settings.INITIATING_CURRENCY_CODE
payment_method_code = settings.INITIATION_PAYMENT_METHOD_CODE
country_code = settings.TERMINATING_COUNTRY_CODE
transfer_code = settings.TRANSFER_PREFIX_CODE
fee = settings.FEE


# ENDPOINTS
passport_endpoint = settings.PASSPORT_ENDPOINT
purchase_endpoint = settings.PURCHASE_ENDPOINT
cardinal_endpoint = settings.CARDINAL_ENDPOINT
access_token = settings.ACCESS_TOKEN


def gen_trans_code():
    a = []
    for i in range(5):
        num = randrange(0,999)
        a.append(str(num))
    new_num = ''.join(a)
    return int(new_num)


def timestamp():
    """function that genrates time stamp"""
    return str((int(timezone.datetime.now().timestamp())))


def signatureCipher(request_method='POST',url=None):
    """this function calculates the signature for other payments"""
    url = quote(url, safe='')
    time_stamp = timestamp()
    nonce = uuid.uuid4().hex
    httpMethod = request_method
    authorisation = "InterswitchAuth" + " " + str(base64.b64encode((client_id).encode("utf-8"))).split('b')[1].split("'")[1]
    signature = "{}&{}&{}&{}&{}&{}".format(httpMethod, url, time_stamp, nonce, client_id, secret_key)
    signatureCipher = base64.b64encode(hashlib.sha1(str(signature).encode()).digest()).decode()
    return (signatureCipher,nonce,time_stamp)


def signatureCipherFundTransfer(request_method='POST',url=None):
    """this function calculates the signature for other payments"""
    url = quote(url, safe='')
    time_stamp = timestamp()
    nonce = uuid.uuid4().hex
    httpMethod = request_method
    authorisation = "InterswitchAuth" + " " + str(base64.b64encode((client_id_fund_transfer).encode("utf-8"))).split('b')[1].split("'")[1]
    signature = "{}&{}&{}&{}&{}&{}".format(httpMethod, url, time_stamp, nonce, client_id_fund_transfer,secret_key_fund_transfer)
    signatureCipher = base64.b64encode(hashlib.sha1(str(signature).encode()).digest()).decode()
    return (signatureCipher,nonce,time_stamp,authorisation)


def signatureCipherRecurrent(request_method='POST',url=None):
    """this function calculates the signature for other payments"""
    url = quote(url, safe='')
    time_stamp = timestamp()
    nonce = uuid.uuid4().hex
    httpMethod = request_method

    signature = "{}&{}&{}&{}&{}&{}".format(httpMethod, url, time_stamp, nonce, client_id_recurrent, secret_key_recurrent)
    signatureCipher = base64.b64encode(hashlib.sha1(str(signature).encode()).digest()).decode()
    return (signatureCipher,nonce,time_stamp)

def signatureCipherBasic(request_method='POST',url=None,amount=None,authdata=None):
    """this function calculates the signature for basic purchases"""
    url = quote(url, safe='')
    httpMethod = request_method
    time_stamp = timestamp()
    nonce = uuid.uuid4().hex
    authorisation = "InterswitchAuth" + " " + str(base64.b64encode((client_id).encode("utf-8"))).split('b')[1].split("'")[1]
    signature = "{}&{}&{}&{}&{}&{}&{}&{}".format(httpMethod, url, time_stamp, nonce, client_id, secret_key, amount, authdata)
    signatureCipher = base64.b64encode(hashlib.sha1(str(signature).encode()).digest()).decode()
    return (signatureCipher,nonce,time_stamp)



def calAuth():
    """this function calculates interswitch authorisation token"""
    hash_details = str(base64.b64encode((client_id + ':' + secret_key).encode("utf-8")))
    authorization = "Basic" + " " + hash_details.split("b'")[1].split("'")[0]
    return authorization

def calAuthFundTransfer():
    """this function calculates interswitch authorisation token"""
    hash_details = str(base64.b64encode((client_id_fund_transfer + ':' + secret_key_fund_transfer).encode("utf-8")))
    authorization = "Basic" + " " + hash_details.split("b'")[1].split("'")[0]
    return authorization


def calAuthRecurrent():
    """this function calculates interswitch authorisation token"""
    hash_details = str(base64.b64encode((client_id_recurrent + ':' + secret_key_recurrent).encode("utf-8")))
    authorization = "Basic" + " " + hash_details.split("b'")[1].split("'")[0]
    return authorization

def getAccessTokenRecurrent():
    """this function return the passport access details"""
    authorisation = calAuthRecurrent()
    url = passport_endpoint + '/passport/oauth/token'
    headers = {'Authorization':authorisation, 'Content-Type':'application/x-www-form-urlencoded'}
    data = {'grant_type': 'client_credentials'}
    make_request = requests.post(url, data=data, headers=headers)
    token = make_request.json()
    return token


def getAccessToken():
    """this function return the passport access details"""
    authorisation = calAuth()
    url = passport_endpoint + '/passport/oauth/token'
    headers = {'Authorization':authorisation, 'Content-Type':'application/x-www-form-urlencoded'}
    data = {'grant_type': 'client_credentials'}
    make_request = requests.post(url, data=data, headers=headers)
    token = make_request.json()
    return token

def getAccessTokenFundTransfer():
    """this function return the passport access details"""
    authorisation = calAuthFundTransfer()
    url = passport_endpoint + '/passport/oauth/token'
    headers = {'Authorization':authorisation, 'Content-Type':'application/x-www-form-urlencoded'}
    data = {'grant_type': 'client_credentials','scope':'profile'}
    make_request = requests.post(url, data=data, headers=headers)
    token = make_request.json()
    print(token)
    return token



def getAuthData(authdata_version=1,pan=None,exp_date=None,cvv=None,pin=None):
    auth_data_cipher = str(authdata_version)+'Z'+str(pan)+'Z'+str(pin)+'Z'+str(exp_date)+'Z'+str(cvv)
    modulus = int(public_modulus,16)
    exponent = int(public_exponent,16)
    n = modulus
    e = exponent
    key_params = (n, e)
    private_key = RSA.construct(key_params)
    # public_key = private_key.publickey().exportKey().decode()
    # rsa_key = RSA.importKey(public_key)
    # print(encrypted_data)
    cipher = PKCS1_v1_5.new(private_key)
    encrypted_data = cipher.encrypt(auth_data_cipher.encode())
    auth_data = base64.b64encode(encrypted_data).decode('utf-8')
    return auth_data


def getMac(init_amount=None):
    init_currency_code = settings.INITIATING_CURRENCY_CODE
    init_payment_method_code = settings.INITIATION_PAYMENT_METHOD_CODE
    terminating_amount = init_amount
    terminating_currency_code = settings.TERMINATING_CURRENCY_CODE
    terminating_payment_method_code = settings.TERMINATING_PAYMENT_METHOD_CODE
    terminating_country_code = settings.TERMINATING_COUNTRY_CODE
    mac_cipher = "{}{}{}{}{}{}{}".format(init_amount,init_currency_code,init_payment_method_code,
                                               terminating_amount,terminating_currency_code,terminating_payment_method_code,
                                               terminating_country_code)
    mac = hashlib.sha512(mac_cipher.encode()).hexdigest()
    return str(mac)

