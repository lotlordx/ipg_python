

def interswitch_errors(make_purchase):
    """Standard Error log for interswitch"""
    if make_purchase['errors'][0]['code'] == 'E43':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'card number is invalid, kindly check and retry.'}}

    elif make_purchase['errors'][0]['code'] == 'X03':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'Amount requested is greater than daily transaction limit'}}

    elif make_purchase['errors'][0]['code'] == '75':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'PIN tries exceeded'}}

    elif make_purchase['errors'][0]['code'] == '10400':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {
                       'message': 'Card has Expired or ExpiryDate, Cvv or Pin format is incorrect, Kindly confirm and try again.'}}

    elif make_purchase['errors'][0]['code'] == 'E58':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'ExpiryDate is incorrect '}}

    elif make_purchase['errors'][0]['code'] == '51':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'insufficent funds in account to complete transaction.'}}

    elif make_purchase['errors'][0]['code'] == '56':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'No card record found.'}}

    elif make_purchase['errors'][0]['code'] == '61':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'Amount requested exceeds withdrawal limit.'}}

    elif make_purchase['errors'][0]['code'] == '55':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'pin supplied is incorrect. kindly check and retry.'}}

    elif make_purchase['errors'][0]['code'] == 'E42':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {
                       'message': 'An error occured in processing your transaction, kindly confirm details and retry.'}}

    elif make_purchase['errors'][0]['code'] == '01':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'An error occured kindly refer to card issuer.'}}

    elif make_purchase['errors'][0]['code'] == 'E18':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {
                       'message': 'The service provider is unreachable at the moment, please try again later.'}}

    elif make_purchase['errors'][0]['code'] == 'E41':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {
                       'message': 'Currency not yet supported.'}}

    elif make_purchase['errors'][0]['code'] == '-2':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {
                       'message': 'An OTP related error has occured, please contact support.'}}

    elif make_purchase['errors'][0]['code'] == '91':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'Issuer or switch inoperative.'}}

    elif make_purchase['errors'][0]['code'] == 'XS1':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'Your payment has exceeded the time required to pay.'}}

    elif make_purchase['errors'][0]['code'] == 'E57':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'The PIN contains an invalid character.'}}

    elif make_purchase['errors'][0]['code'] == 'E19':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'An invalid response was received from remote host, please contact support.'}}

    if make_purchase['errors'][0]['code'] == 'Z5':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'Payment has already been Processed'}}

    elif make_purchase['errors'][0]['code'] == 'T1':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'An error occured in processing this transaction'}}

    elif make_purchase['errors'][0]['code'] == '-2':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'An OTP related error has occured kindly contact support'}}

    elif make_purchase['errors'][0]['code'] == 'X03':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'Amount requested is greater than daily transaction limit'}}

    elif make_purchase['errors'][0]['code'] == 'E21':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'An unknown error has occurred, please contact system administrator.'}}

    elif make_purchase['errors'][0]['code'] == '13':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'Invalid Amount.'}}

    elif make_purchase['errors'][0]['code'] == '57':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'Transaction not permitted to Card holder.'}}

    elif make_purchase['errors'][0]['code'] == '59':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'Transaction Failed.'}}

    elif make_purchase['errors'][0]['code'] == 'Z81':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'No bin was found for this card number'}}

    elif make_purchase['errors'][0]['code'] == '10409':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'Payment already completed'}}

    elif make_purchase['errors'][0]['code'] == 'X04':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'Amount does not meet minimum amount allowed'}}

    elif make_purchase['errors'][0]['code'] == 'Z8':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'Card type has not been configured for payment gateway'}}

    elif make_purchase['errors'][0]['code'] == '10500':
        context = {'status': False, 'message': 'An error Occured',
                   'data': {'message': 'Error processing request, please try again'}}


    return context
