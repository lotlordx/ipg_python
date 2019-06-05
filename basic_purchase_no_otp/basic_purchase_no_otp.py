import requests, json
from calculations import signatureCipherBasic,getAccessToken,access_token,purchase_endpoint
import time
import calendar



def make_no_otp_payment(trans_ref=None,amount=None,authData=None,cust_id=None):
    """To accept payment with card without One Time Password (OTP) use this end point to make your request."""
    url = purchase_endpoint + '/api/v3/purchases'
    content_type = 'application/json'
    token = getAccessToken()['access_token']
    authorisation = 'Bearer {}'.format(token)
    signature, nonce,time_stamp = (signatureCipherBasic(url=url, amount=amount, authdata=authData))
    signature_method = 'SHA1'
    authkeyversion = '1'
    headers = {'Content-Type':content_type, 'Authorization':authorisation, 'Timestamp':time_stamp,'Nonce':nonce,
               'Signature':signature, 'SignatureMethod':signature_method, 'AuthKeyVersion':authkeyversion}

    data = {'customerId': cust_id,'amount':amount,'authData':authData,'currency': 'NGN','transactionRef': trans_ref}
    make_request = requests.post(url, data=json.dumps(data), headers=headers)
    recurrent_token = make_request.json()
    return recurrent_token


def validate_card_payment_otp(payment_id,authData,otp):
    """this function validates a card is the response code is TO """
    url = purchase_endpoint + '/api/v3/purchases/otps/auths'
    content_type = 'application/json'
    token = getAccessToken()['access_token']
    authorisation = 'Bearer {}'.format(token)
    signature, nonce,time_stamp = (signatureCipherBasic(url=url, amount=otp, authdata=authData))
    signature_method = 'SHA1'
    authkeyversion = '1'
    headers = {'Content-Type':content_type, 'Authorization':authorisation, 'Timestamp':time_stamp,'Nonce':nonce,
               'Signature':signature, 'SignatureMethod':signature_method, 'AuthKeyVersion':authkeyversion}
    data = {'paymentId':payment_id, 'authData':authData, 'otp':otp}
    make_request = requests.post(url, data=json.dumps(data), headers=headers)
    validate_otp = make_request.json()
    return validate_otp