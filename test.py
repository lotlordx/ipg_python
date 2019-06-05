from recurring_payments.recurring_payments import recurrent_tokenz,recurrent_purchase,get_transaction_status,get_transaction_status_v2
from card_validation.card_validation import validate_card
from validate_bank.validate_bankaccount_number import validate_bankaccount_number
from visa_cardinal.visa_cardinal import visa_purchase
from calculations import getAuthData
from calculations import signatureCipher
from basic_purchase_no_otp.basic_purchase_no_otp import make_no_otp_payment
from calculations import timestamp
from fund_transfer.tools import validate_account,get_all_banks

trans_ref = 'JB-{}-ReccValid'.format(timestamp())
amount = '0.1'
authData = 'mQBHno1V+hf168MO7+cHmeM5VB2hvvjeffME2TptKk3zsawBT6Wx5emOOKSxY/THnKdnWfAgXlRSYhE509ultSYrHt8+8HmqCHPSE+aezgOCOjdVgqIgncgCT6fefCCC1moelTS6+KZ4XHzO6sKNOlYv0H2ZNY5FayLGmXeMP62omTLgO4i+Rrr0F6EtsFIjq2aOyHmwI56KXp4vo3aFol+0fXiB16LNBw6Wp82neTQRizO3EohVDt37IhxUGYQb/VfhQKoWWgyYF/lejTsz28aPM/SAdyj+FUizCEAA9re1HjFrFCVRf58n277zc/HxsawRtUQzUwcE3Al9Nv30/A=='

# authData = 'AYNIJozH87EXX19408GTQhxaxXYpL75SqVUjXVwXz979Ejeg+gVI09nyWJFj/y3wTwuOlyFs7ztCCbB4YrcrA3xi5Nkpd5crk9PWyGIlEsOziJZQ+BnRMvRikhHpVZheNbwtooq75ggtoAZ3fQrsCQq/uRjLeTNHhPr3rztzx71Ay5DzsJRrEFFvSXlafv5Ev/wo4r8Y03gfVlrivruIzKNFr1X1hogtj40JatXW2W9BjVAzwspiF920Sf2KVKUG1Nmus1llUqOTI8k+z7/+MsYDgYSKnnH3rKdnJdM7cSlR/hKWozKxrEG/+rztw4WRThk+QJi2YRIdJgqCsM1HJw=='
authData1 = "jGyoTA/JJJOf/12MMd/1ypK9Av6yJXB7BiJZjEkA2tOQSnAGUOY764QybjZ24MTVWC08YOc6SJOfBQ+ZmQ/6p5nc3uIAlbVYD8/" \
            "Bp67RLcu6EfQsfnRU7me1X4Kz4g2mBaMZWy9xYXIuVEz0PIgQlPQ3OW+87SS3uDYGojpWrT5uNi2G24JilKLCx6pX1bl3Cyy1YLNyw" \
            "3aIk+Hs+lT2C2bNZjyTn4DAN2kSUCtEpK+1H3azjt7RJZ0ZU9eeRNHSrduurMISykdzkTR+TEfW1mQd914YBTCbaDJev6pMff0L25/" \
            "ffftUdHM+5mmBmHiE8B2LN2FKlOSDZQ4/AKlCkQ=="



# pan = 5061030000000000084
# pan = 5060990580000217499
# valid card details
# pan = 6280511000000095

# pan = 4000000000000002
# exp_date = 2005
# cvv = 123
# pin = 1111

# trans_ref = 'JB-{}-ReccValid'.format(timestamp)
# amount = 90

# auth_data = getAuthData(pan=pan,exp_date=exp_date,cvv=cvv,pin=pin)

# signatureCipher(url='https://sandbox.interswitchng.com/api/v2/purchases/validations/recurrents')

# recurrent = recurrent_tokenz(trans_ref=trans_ref,authData=authData)
# validate_request(trans_ref=trans_ref,amount=amount,authData=authData)
# make_no_otp_payment(trans_ref=trans_ref,amount=amount,authData=auth_data,cust_id='lotanna.camaechi@gmail.com')
# trans_ref = 'MBG-1538076033-REC'
# recurrent_purchase(trans_ref=trans_ref,amount=5000,card_token=recurrent['token'],card_expiry=recurrent['tokenExpiryDate'],cust_id='test@gmail.com')
# recurrent_purchase(trans_ref=trans_ref,amount=5000,card_token=token,card_expiry=token_expiry,cust_id='test@gmail.com')
# get_transaction_status(trans_ref='JB-1517239112-NoOTP',amount=amount)
# get_transaction_status_v2(amount=amount,trans_ref='JB-1534084152-NoOTP')
# validate_bankaccount_number(bank_code='063',account_number='0024220630')
# get_all_banks()
# validate_account()
# validate_card(trans_ref=trans_ref,amount=amount,authData=authData)
# visa_purchase(trans_ref=trans_ref, amount=amount, authData=auth_data,cust_id='hello')
# get_transaction_status(trans_ref='MBG-1538572024-REC',amount=1000)

