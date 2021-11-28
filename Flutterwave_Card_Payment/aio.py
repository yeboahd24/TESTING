import requests
import pin
import os


secret_key = os.environ.get('FLUTTERWAVE_SECRET_KEY')
public_key = os.environ.get('FLUTTERWAVE_PUBLIC_KEY')
url = 'https://api.flutterwave.com/v3/payments'


def flutterwave_payment():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + secret_key
    }

    data = {
        "tx_ref": "hooli-tx-1997bbtytty",
        "amount": "100",
        "currency": "NGN",
        "redirect_url": "https://webhook.site/9d0b00ba-9a69-44fa-a43d-a82c33c36fdc",
        "payment_options": "card",
        "meta": {
            "consumer_id": 23,
            "consumer_mac": "92a3-912ba-1192a"
        },
        "customer": {
            "email": "yeboahd24@gmail.com",
            "phonenumber": "08088884528",
            "name": "Yemi Desola"
        },
        "customizations": {
            "title": "Pied Piper Payments",
            "description": "Middleout isn't free. Pay the price",
            "logo": "https://assets.piedpiper.com/logo.png"
        }
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.json()['data']['link'])


flutterwave_payment()
