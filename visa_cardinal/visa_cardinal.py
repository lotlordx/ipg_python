import requests, json
from calculations import signatureCipherBasic,signatureCipher,access_token,getAccessToken,purchase_endpoint,cardinal_endpoint



def visa_purchase(trans_ref=None,amount=None,authData=None,cust_id=None):
    """this function allow you to make a recurrent purchase"""
    url = purchase_endpoint + '/api/v3/purchases'
    content_type = 'application/json'
    token = getAccessToken()['access_token']
    authorisation = 'Bearer {}'.format(token)
    signature, nonce,time_stamp = signatureCipherBasic(url=url,amount=amount,authdata=authData)
    signature_method = 'SHA1'
    authkeyversion = '1'

    headers = {'Content-Type':content_type, 'Authorization':authorisation, 'Timestamp':time_stamp,'Nonce':nonce,
               'Signature':signature, 'SignatureMethod':signature_method, 'AuthKeyVersion':authkeyversion}
    data = {'transactionRef': trans_ref,'amount':amount, 'authData':authData,'currency':'NGN',
            'customerId':cust_id}

    make_request = requests.post(url, data=json.dumps(data), headers=headers)
    visa_purchase = make_request.json()
    print(visa_purchase)
    return visa_purchase


def isw_callback(md=None, pa_res=None):
    """this function allow you to make a recurrent purchase"""
    url = cardinal_endpoint + '/collections/api/v1/pay/cardinalCallBack'

    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding':'gzip, deflate, br',
               'Accept-Language':'fr-FR,fr;q=0.9,en-GB;q=0.8,en;q=0.7,fr-CA;q=0.6,en-US;q=0.5',
               'Content-Length':'4170',
               'Content-Type':'application/x-www-form-urlencoded',
               'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}

    data = {'MD': md,'PaRes':pa_res}

    make_request = requests.post(url, data=data, headers=headers)
    visa_purchase = make_request.status_code
    print(visa_purchase)
    if visa_purchase == 200:
        return True
    else:
        return False


def otp_validation(payment_id=None, transaction_id=None,eci_flag=None):
    """this function validates the isw request on request to the page """

    url = purchase_endpoint + '/api/v3/purchases/otps/auths'
    content_type = 'application/json'
    token = getAccessToken()['access_token']
    authorisation = 'Bearer {}'.format(token)
    signature, nonce,time_stamp = signatureCipher(url=url)
    signature_method = 'SHA1'
    authkeyversion = '1'

    headers = {'Content-Type':content_type, 'Authorization':authorisation, 'Timestamp':time_stamp,'Nonce':nonce,
               'Signature':signature, 'SignatureMethod':signature_method, 'AuthKeyVersion':authkeyversion}
    data = {'paymentId': str(payment_id),'transactionId':str(transaction_id), 'eciFlag':str(eci_flag)}

    make_request = requests.post(url, data=json.dumps(data), headers=headers)
    visa_purchase = make_request.json()
    return visa_purchase


