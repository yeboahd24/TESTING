import os

os.environ['FLUTTERWAVE_URL'] = 'https://api.flutterwave.com/v3/charges?type=card'
os.environ['FLUTTERWAVE_SECRET_KEY'] = 'FLWSECK_TEST-88ebd2a6edb534bbc663d33efcd1211a-X'
os.environ['FLUTTERWAVE_PUBLIC_KEY'] = 'FLWPUBK_TEST-2b7e49c0934300756e2fdb4ecb55f718-X'
os.environ['FLUTTERWAVE_MOBILE_URL'] = 'https://api.flutterwave.com/v3/charges?type=mobile_money_ghana'
os.environ['FLUTTERWAVE_VERIFICATION_URL'] = 'https://api.flutterwave.com/v3/transactions/verify'
