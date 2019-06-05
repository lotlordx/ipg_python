import requests, json
from calculations import signatureCipherFundTransfer,getAccessTokenFundTransfer,access_token,purchase_endpoint


def validate_bankaccount_number(account_number=None,bank_code=None):
    """this function allow you to get a transaction status"""
    url = purchase_endpoint + '/api/v1/nameenquiry/banks/accounts/names'
    content_type = 'application/json'
    # token = getAccessTokenFundTransfer()['access_token']
    # authorisation = 'Bearer {}'.format(token)
    signature, nonce, time_stamp, authorisation = (signatureCipherFundTransfer(request_method='GET', url=url))
    signature_method = 'SHA1'
    headers = {'Content-Type':content_type, 'Authorization':authorisation, 'Timestamp':time_stamp,'Nonce':nonce,
               'Signature':signature, 'SignatureMethod':signature_method,'bankCode':bank_code,'accountId':account_number}

    make_request = requests.get(url, headers=headers)
    validate_bank = make_request.json()
    return validate_bank
