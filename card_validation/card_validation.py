import requests, json
from calculations import signatureCipher,signatureCipherRecurrent,getAccessToken,getAccessTokenRecurrent,access_token,purchase_endpoint


def validate_card(trans_ref,authData):
    """this function validates a card and brings out all the details of a card"""
    url = purchase_endpoint + '/api/v3/purchases/validations'
    print(url)
    content_type = 'application/json'
    token = getAccessToken()['access_token']
    # print(token)
    authorisation = 'Bearer {}'.format(token)
    signature, nonce,time_stamp = (signatureCipher(url=url))
    signature_method = 'SHA1'
    authkeyversion = '1'
    headers = {'Content-Type':content_type, 'Authorization':authorisation, 'Timestamp':time_stamp,'Nonce':nonce,
               'Signature':signature, 'SignatureMethod':signature_method, 'AuthKeyVersion':authkeyversion}
    data = {'transactionRef': trans_ref, 'authData':authData}
    make_request = requests.post(url, data=json.dumps(data), headers=headers)
    validate_request = make_request.json()
    print(validate_request)
    return validate_request


def validate_card_otp(trans_ref,otp):
    """this function validates a card is the response code is TO """
    url = purchase_endpoint + '/api/v3/purchases/validations/otps/auths'
    content_type = 'application/json'
    token = getAccessToken()['access_token']
    authorisation = 'Bearer {}'.format(token)
    signature, nonce,time_stamp = (signatureCipher(url=url))
    signature_method = 'SHA1'
    authkeyversion = '1'
    headers = {'Content-Type':content_type, 'Authorization':authorisation, 'Timestamp':time_stamp,'Nonce':nonce,
               'Signature':signature, 'SignatureMethod':signature_method, 'AuthKeyVersion':authkeyversion}
    data = {'transactionRef': trans_ref, 'otp':otp}
    make_request = requests.post(url, data=json.dumps(data), headers=headers)
    validate_otp = make_request.json()
    print(validate_otp)
    return validate_otp


def validate_mobile_number(payment_id,trans_ref,mobile_number):
    """this function validates a card is the response code is MO """
    url = purchase_endpoint + '/api/v3/purchases/otps/enrollments'
    content_type = 'application/json'
    token = getAccessToken()['access_token']
    authorisation = 'Bearer {}'.format(token)
    signature, nonce,time_stamp = (signatureCipher(url=url))
    signature_method = 'SHA1'
    authkeyversion = '1'
    headers = {'Content-Type':content_type, 'Authorization':authorisation, 'Timestamp':time_stamp,'Nonce':nonce,
               'Signature':signature, 'SignatureMethod':signature_method, 'AuthKeyVersion':authkeyversion}
    data = {'paymentId': payment_id, 'mobilePhoneNumber':mobile_number, 'transactionRef':trans_ref}
    make_request = requests.post(url, data=json.dumps(data), headers=headers)
    validate_otp = make_request.json()
    print(validate_otp)
    return validate_otp