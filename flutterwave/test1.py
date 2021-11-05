
import os
import requests
import json

FLUTTERWAVE_PUBLIC_KEY = os.environ.get("FLUTTERWAVE_PUBLIC_KEY")


def charge_by_card():
    base_url = "https://api.flutterwave.com/v3/charges?type=card"
    headers = {
        'Authorization': f'Bearer {FLUTTERWAVE_PUBLIC_KEY}',
        'Content-Type': 'application/json'
    }

    payload = json.dumps({


   "card_number": "4556052704172643",
   "cvv": "899",
   "expiry_month": "01",
   "expiry_year": "21",
   "currency": "NGN",
   "amount": "100",
   "fullname": "Yemi Desola",
   "email": "user@flw.com",
   "tx_ref": "MC-3243e",
   "redirect_url": "https://webhook.site/3ed41e38-2c79-4c79-b455-97398730866c",
   "authorization": {
      "mode": "pin",
      "pin": "3310"
   }


    })

    response = requests.request(
        "POST", url = base_url, headers = headers, data = payload)
    print(response.text())

charge_by_card()