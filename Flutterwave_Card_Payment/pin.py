import os

os.environ['FLUTTERWAVE_URL'] = 'https://api.flutterwave.com/v3/charges?type=card'
os.environ['FLUTTERWAVE_SECRET_KEY'] = 'FLWSECK_TEST-88ebd2a6edb534bbc663d33efcd1211a-X'
os.environ['FLUTTERWAVE_PUBLIC_KEY'] = 'FLWPUBK_TEST-2b7e49c0934300756e2fdb4ecb55f718-X'
os.environ['FLUTTERWAVE_MOBILE_URL'] = 'https://api.flutterwave.com/v3/charges?type=mobile_money_ghana'
os.environ['FLUTTERWAVE_VERIFICATION_URL'] = 'https://api.flutterwave.com/v3/transactions/verify'
# os.environ['HTTPS_PROXY'] = "https://Yeboah:maryyeboah70@tnttukbbvmi.sandbox.verygoodproxy.com:8443"


username = 'US2NvgTaRvSfTB2tmp1hBktH'
passwd = '15410431-a06b-46f2-b69e-8d36491d93d0'
vault = 'tnttukbbvmi'


os.environ['HTTPS_PROXY'] = 'http://' + username + ':' + passwd + '@' + vault + '.sandbox.verygoodproxy.com:8080'

