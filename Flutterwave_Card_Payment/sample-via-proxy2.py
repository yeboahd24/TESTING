import os
import requests

username = 'US2NvgTaRvSfTB2tmp1hBktH'
passwd = '15410431-a06b-46f2-b69e-8d36491d93d0'
vault = 'tnttukbbvmi'

os.environ['HTTPS_PROXY'] = 'http://' + username + ':' + passwd + '@' + vault + '.sandbox.verygoodproxy.com:8080'

response = requests.post('https://api.flutterwave.com/v3/charges?type=card',
                         headers={
                            "Content-type": "application/json",
                            "Secret-Key": "tok_sandbox_rVdCJgokR3bK7EdXU3d1hs",
                         },
                         json={
                             "amount": 100,
                             "card_number": "tok_sandbox_5xCjcCyYWchHkSNfkmnFBv",
                             "cvv": "tok_sandbox_sYrvCZHFxgNb8c7p5WfKS9",
                             "expiry_month": "09",
                             "expiry_year": "34",
                             "currency": "GHS",
                             "country": "GH",
                             "redirect_url": "https://webhook.site/c1ff1154-8535-4d1a-99a6-5b32cc5c366d",
                             "email": "yeboahd24@gmail.com",
                             "phone_number": "0540303211",
                             "preauthorize": "True",
                             "tx_ref": "MC-3243e",
                             "authorization": {
                                 "mode": "pin",
                                 "pin": "3310"
                             }
                         },
                         verify="TESTING/Flutterwave_Card_Payment/sandbox.pem")
print(str(response.text))
