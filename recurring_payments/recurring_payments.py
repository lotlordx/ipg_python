import requests, json
from calculations import signatureCipherRecurrent,getAccessTokenRecurrent,access_token,purchase_endpoint
from django.utils import timezone


def recurrent_tokenz(authData):
    """this function gets the recurrent token details"""
    url = purchase_endpoint + '/api/v2/purchases/validations/recurrents'
    content_type = 'application/json'
    token = getAccessTokenRecurrent()['access_token']
    authorisation = 'Bearer {}'.format(token)
    trans_ref = 'MBG-{}-REC'.format(str(int(timezone.now().timestamp())))
    signature, nonce, time_stamp = (signatureCipherRecurrent(url=url))
    signature_method = 'SHA1'
    authkeyversion = '1'
    headers = {'Content-Type':content_type, 'Authorization':authorisation, 'Timestamp':time_stamp,'Nonce':nonce,
               'Signature':signature, 'SignatureMethod':signature_method, 'AuthKeyVersion':authkeyversion}
    data = {'transactionRef': trans_ref, 'authData':authData}
    make_request = requests.post(url, data=json.dumps(data), headers=headers)
    recurrent_token = make_request.json()
    return recurrent_token


def recurrent_purchase(trans_ref=None,amount=None,card_token=None,card_expiry=None,cust_id=None):
    """this function allow you to make a recurrent purchase"""
    url = purchase_endpoint + '/api/v2/purchases/recurrents'
    content_type = 'application/json'
    token = getAccessTokenRecurrent()['access_token']
    # print(token)
    authorisation = 'Bearer {}'.format(token)
    # print(authorisation)
    signature, nonce,time_stamp = (signatureCipherRecurrent(url=url))
    signature_method = 'SHA1'
    authkeyversion = '1'

    headers = {'Content-Type':content_type, 'Authorization':authorisation, 'Timestamp':time_stamp,'Nonce':nonce,
               'Signature':signature, 'SignatureMethod':signature_method, 'AuthKeyVersion':authkeyversion}
    data = {'transactionRef': trans_ref,'amount':str(amount),'currency':'NGN', 'token':str(card_token),
            'tokenExpiryDate':str(card_expiry),'customerId':cust_id}

    make_request = requests.post(url, data=json.dumps(data), headers=headers)
    recurrent_purchase = make_request.json()
    return recurrent_purchase


def get_transaction_status(trans_ref=None,amount=None):
    """this function allow you to get a transaction status"""
    url = purchase_endpoint+ '/api/v3/purchases'
    content_type = 'application/json'
    token = getAccessTokenRecurrent()['access_token']
    authorisation = 'Bearer {}'.format(token)
    signature, nonce,time_stamp = (signatureCipherRecurrent(request_method='GET', url=url))
    signature_method = 'SHA1'
    authkeyversion = '1'
    headers = {'Amount':str(amount),'transactionRef':trans_ref,'Content-Type':content_type, 'Authorization':authorisation, 'Timestamp':time_stamp,'Nonce':nonce,
               'Signature':signature, 'SignatureMethod':signature_method, 'AuthKeyVersion':authkeyversion}

    make_request = requests.get(url, headers=headers)
    trans_status = make_request.json()
    print(trans_status)
    return trans_status

def get_transaction_status_v2(trans_ref=None,amount=None):
    """this function allow you to get a transaction status version 2"""
    url = 'https://sandbox.interswitchng.com/collections/api/v1/gettransaction.json'
    params = {'getacquirerdata':True, 'transactionreference':trans_ref, 'amount':str(amount),'merchantcode':getAccessTokenRecurrent()['merchant_code']}
    make_request = requests.get(url, params=params)
    trans_status_v2 = make_request.json()
    return trans_status_v2