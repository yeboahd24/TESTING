import os
import requests


username = 'US23gEttViX2hkm8ipMseVis'
passwd = '162b081b-35fc-4890-a00f-9736da987464'
vault = 'tnttukbbvmi'

os.environ['HTTPS_PROXY'] = 'http://' + username + ':' + passwd + '@' + vault + '.SANDBOX.verygoodproxy.com:8080'


#"Authorization":'Bearer FLWSECK_TEST-88ebd2a6edb534bbc663d33efcd1211a-X',
# 'https://echo.apps.verygood.systems/post'
# 'https://api.flutterwave.com/v3/charges?type=card'
# os.environ['HTTPS_PROXY']=  'https://USERNAME:PASSWORD@tnttukbbvmi.sandbox.verygoodproxy.com:8443'

response = requests.post('https://api.flutterwave.com/v3/charges?type=card',
                         headers={
                            "Content-type": "application/json",
                            "X-Private-Key": "tok_sandbox_4pXY0grBDyaqeiAAwQ7T5g",
                         },
                         json={
                            "PBFPubKey": "FLWSECK_TEST-88ebd2a6edb534bbc663d33efcd1211a-X",
                            "card_number": "tok_sandbox_4pXY0grBDyaqeiAAwQ7T5g",
                            "cvv": "564",
                            "expirymonth": "09",
                            "expiryyear": "19",
                            "currency": "NGN",
                            "country": "NG",
                            "amount": "20",
                            "email": "yeboahd24@gmail.com",
                            "phonenumber": "0902620185",
                            "firstname": "temi",
                            "lastname": "desola",
                            "IP": "355426087298442",
                            "txRef": "MC-2021-09-13",
                            "meta": [{"metaname": "flightID", "metavalue": "123949494DC"}],
                            "redirect_url": "https://rave-webhook.herokuapp.com/receivepayment",
                            "device_fingerprint": "69e6b7f0b72037aa8428b70fbe03986c",
                            "pin": "3310",

                         }, verify='Flutterwave_Card_Payment/sandbox.pem')
print(str(response.text))

