import requests
from calculations import signatureCipherFundTransfer,getAccessToken,\
    purchase_endpoint,getAccessTokenFundTransfer,getMac,client_id_fund_transfer,terminal_id,entity_code,gen_trans_code,\
    currency_code,payment_method_code,country_code,transfer_code,fee,access_token
import base64
import json


def get_all_banks():
    """this function return all banks supported by interswitch"""

    url = purchase_endpoint + "/api/v2/quickteller/configuration/fundstransferbanks"
    token = getAccessTokenFundTransfer()['access_token']
    content_type = 'application/json'
    # authorisation = 'Bearer {}'.format(token)
    signature, nonce, time_stamp, authorisation = (signatureCipherFundTransfer(request_method='GET', url=url))
    headers = {'Authorization':authorisation,'Content-Type':content_type, 'Timestamp':time_stamp,'Nonce':nonce}
    make_request = requests.get(url, headers=headers)
    validate_account = make_request.json()
    print(validate_account)
    return validate_account

# get_all_banks()


def validate_account():
    bank_code = '058'
    account_number = '0138624908'
    url = purchase_endpoint+"/api/v1/nameenquiry/banks/"+bank_code+"/"+"accounts/"+account_number+"/names"
    token = getAccessTokenFundTransfer()['access_token']
    # authorisation = 'Bearer {}'.format(token)
    signature, nonce, time_stamp, authorisation = (signatureCipherFundTransfer(request_method='GET', url=url))
    signature_method = 'SHA1'
    headers = {'Authorization':authorisation, 'Timestamp':time_stamp,'Nonce':nonce,
               'Signature':signature, 'SignatureMethod':signature_method}

    make_request = requests.get(url, headers=headers)
    validate_account = make_request.json()
    # print(validate_account)
    return validate_account


def send_funds(init_amount=None, beneficiary={}, account_details={},bank_code=None):
    url = purchase_endpoint + '/api/v2/quickteller/payments/transfers'
    content_type = 'application/json'
    # authorisation = "InterswitchAuth" + " " + str(base64.b64encode((client_id_fund_transfer).encode("utf-8"))).split('b')[1].split("'")[1]
    signature, nonce, time_stamp, authorisation = (signatureCipherFundTransfer(request_method='GET', url=url))
    signature_method = 'SHA1'

    mac = getMac(init_amount=int(float(init_amount)*100))
    initiating_entity_code = entity_code
    initiation = {"amount":int(float(init_amount)*100),"channel": "7","currencyCode":currency_code,"paymentMethodCode":payment_method_code,
                  }
    sender = {"email": "info@nuture.tech","lastname": "Nuture","othernames": "Technology Services","phone": "09066582734"}
    termination = {"accountReceivable":account_details,"amount":int(float(init_amount)*100),"countryCode":country_code,
                   "currencyCode": "566", "entityCode": bank_code, "paymentMethodCode": "AC"
                   }
    transferz_code = '{}{}'.format(transfer_code,gen_trans_code())

    headers = {'Content-Type':content_type, 'Authorization':authorisation, 'Timestamp':time_stamp,'Nonce':nonce,
               'Signature':signature, 'SignatureMethod':signature_method, 'TerminalID':terminal_id}
    data = {'mac': mac,'beneficiary':beneficiary, 'initiatingEntityCode':initiating_entity_code,
            'initiation':initiation, 'sender':sender,'termination':termination,'surcharge':'10000','transferCode':transferz_code}

    make_request = requests.post(url, data=json.dumps(data), headers=headers)
    send_fund = make_request.json()
    print(send_fund)
    return send_fund

# send_funds(init_amount=10, beneficiary={"lastname": "Okezie","othernames": "Uchenna"},account_details={"accountNumber": "0014598347","accountType": "10"},
#            bank_code='058')
