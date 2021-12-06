
import os
import requests
import json
import pin
import subprocess


# FLUTTERWAVE_PUBLIC_KEY = os.environ.get("FLUTTERWAVE_PUBLIC_KEY")

# vgs_url = 'https://echo.apps.verygood.systems/post'
# USERNAME = 'maryyeboah70@tnttukbbvmi.sandbox.verygoodproxy.com'

# def charge_by_card():
#     base_url = "https://api.flutterwave.com/v3/charges?type=card"
#     headers = {
#         'Authorization': f'Bearer {FLUTTERWAVE_PUBLIC_KEY}',
#         'Content-Type': 'application/json',
#     }

#     payload = json.dumps({


#    "card_number": "4556052704172643",
#    "cvv": "899",
#    "expiry_month": "01",
#    "expiry_year": "21",
#    "currency": "NGN",
#    "amount": "100",
#    "fullname": "Yemi Desola",
#    "email": "user@flw.com",
#    "tx_ref": "MC-3243e",
#    "redirect_url": "https://webhook.site/3ed41e38-2c79-4c79-b455-97398730866c",
#    "authorization": {
#       "mode": "pin",
#       "pin": "3310"
#    }


#     })

#     response = requests.request(
#         "POST", url = base_url, headers = headers, data = payload)
#     print(response.json())


def subprocess_cmd(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout)
    return proc_stdout
# https://echo.apps.verygood.systems/post -k \
#   -x USERNAME:PASSWORD@VAULT_ID.sandbox.verygoodproxy.com:8080 \
#   -H "Content-type: application/json" \
#   -H "X-Private-Key: tok_sandbox_4b8ascF2V16kpgsaqg3gMy" \
#   -d '{
#   "PBFPubKey": "FLWPUBK-e634d14d9ded04eaf05d5b63a0a06d2f-X",
#   "cardno": "tok_sandbox_gk2pZ3yw71RfLYC1FZkzSd",
#   "cvv": "tok_sandbox_tanbVwBtp9gNgyfFMLb8ui",
#   "expirymonth": "09",
#   "expiryyear": "19",
#   "currency": "NGN",
#   "country": "NG",
#   "amount": "10",
#   "email": "user@gmail.com",
#   "phonenumber": "0902620185",
#   "firstname": "temi",
#   "lastname": "desola",
#   "IP": "355426087298442",
#   "txRef": "MC-2021-09-13",
#   "meta": [{metaname: "flightID", metavalue: "123949494DC"}],
#   "redirect_url": "https://rave-webhook.herokuapp.com/receivepayment"",
#   "device_fingerprint": "69e6b7f0b72037aa8428b70fbe03986c"
# }'


subprocess.call(['curl https://echo.apps.verygood.systems/post -k \
  -x USERNAME:PASSWORD@VAULT_ID.sandbox.verygoodproxy.com:8080 \
  -H "Content-type": "application/json" \
  -H "X-Private-Key: tok_sandbox_4b8ascF2V16kpgsaqg3gMy" \
  'PBFPubKey': 'FLWPUBK-e634d14d9ded04eaf05d5b63a0a06d2f-X'
  "PBFPubKey": "FLWPUBK-e634d14d9ded04eaf05d5b63a0a06d2f-X",
  "cardno": "tok_sandbox_gk2pZ3yw71RfLYC1FZkzSd",
  "cvv": "tok_sandbox_tanbVwBtp9gNgyfFMLb8ui",
  "expirymonth": "09",
  "expiryyear": "19",
  "currency": "NGN",
  "country": "NG",
  "amount": "10",
  "email": "user@gmail.com",
  "phonenumber": "0902620185",
  "firstname": "temi",
  "lastname": "desola",
  "IP": "355426087298442",
  "txRef": "MC-2021-09-13",
  "meta": [{metaname: "flightID", metavalue: "123949494DC"}],
  "redirect_url": "https://rave-webhook.herokuapp.com/receivepayment",
  "device_fingerprint": "69e6b7f0b72037aa8428b70fbe03986c"

