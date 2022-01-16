import os
import requests

# username = 'US4GZonm5BjNKDJUML2odaQ6'
# passwd = 'af9305d0-80ef-4c86-96ee-4f32f7941dce'
# vault = 'tnttukbbvmi'

# os.environ['HTTPS_PROXY'] = 'http://' + username + ':' + \
#     passwd + '@' + vault + '.sandbox.verygoodproxy.com:8080'

# response = requests.post('https://api.flutterwave.com/v3/charges?type=card',
#                          headers={
#                              "Content-type": "application/json",
#                              "Secret-Key": "tok_sandbox_rVdCJgokR3bK7EdXU3d1hs",
#                              # "proxy": "http://" + username + ":" + passwd + "@" + vault + ".sandbox.verygoodproxy.com:8080"
#                          },
#                          json={
#                              "amount": 100,
#                              "card_number": "tok_sandbox_5xCjcCyYWchHkSNfkmnFBv",
#                              "cvv":"tok_sandbox_obQgort9KsrpG2iVLuFzeZ",
#                              "expiry_month": "09",
#                              "expiry_year": "34",
#                              "currency": "GHS",
#                              "country": "GH",
#                              "redirect_url": "https://webhook.site/c1ff1154-8535-4d1a-99a6-5b32cc5c366d",
#                              "email": "yeboahd24@gmail.com",
#                              "phone_number": "0540303211",
#                              "preauthorize": "True",
#                              "tx_ref": "MC-3243e",
#                              "authorization": {
#                                  "mode": "pin",
#                                  "pin": "3310",
#                              }
#                          },
#                          verify="./sandbox.pem")
# print(str(response.text))

# url = "https://api.flutterwave.com/v3/validate-charge"

# payload = {
#     "otp": "12345",
#     "flw_ref": "FLW-MOCK-df67c59cb59d8a657e805bb3c7c16e3a",
#     "type": "card"
# }
# _headers = {
#     "Accept": "application/json",
#     "Authorization": "Bearer FLWSECK_TEST-88ebd2a6edb534bbc663d33efcd1211a-X",
#     "Content-Type": "application/json"
# }

# response2 = requests.request("POST", url, json=payload, headers=_headers)
# print(str(response2.text))


url ="https://api.flutterwave.com/v3/transactions/2826874/verify"
_headers = {
    "Accept": "application/json",
    "Authorization": "Bearer FLWSECK_TEST-88ebd2a6edb534bbc663d33efcd1211a-X",
    "Content-Type": "application/json"
}

response2 = requests.request("GET", url, headers=_headers)
print(str(response2.text))


