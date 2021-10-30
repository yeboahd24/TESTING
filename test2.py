import requests
import os
import secret
import json

PAYSTACK_SECRET_KEY = os.getenv('PAYSTACK_SECRET_KEY')

url = "https://api.paystack.co/charge"

def charge_by_card():

    payload = json.dumps({
        "email": "linux@gmail.com",
        "amount": "10000",
        # "metadata": {
        #     "custom_fields": [
        #     {
        #         "value": "makurdi",
        #         "display_name": "Donation for",
        #         "variable_name": "donation_for"
        #     }
        #     ]
        # },
        "card": {
            "cvv": "408",
            "number": "4084084084084081",
            "expiry_month": "01",
            "expiry_year": "99"
        },
        "pin": "0000",

    })
    headers = {
        'Authorization': f'Bearer {PAYSTACK_SECRET_KEY}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

# charge_by_card()


def initialize_transaction():

    url = "https://api.paystack.co/transaction/initialize"

    payload = json.dumps({
        "email": "linux@email.com",
        "amount": "500000",
    # "reference": "XXXREF",
    # "metadata": {
    #     "custom_fields": [
    #     {
    #         "display_name": "Mobile Number",
    #         "variable_name": "mobile_number",
    #         "value": "+233540303211"
    #     }
    #     ]
    # }
    })
    headers = {
        'Authorization': f'Bearer {PAYSTACK_SECRET_KEY}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

# initialize_transaction()


def mobile_money_transaction():

    url = "https://api.paystack.co/transaction/initialize"

    payload = json.dumps({

        "amount": "1000",
        "email": "dominic@gmail.com",
        "currency": "GHS",
        "mobile_money": {
            "phone" : "+233540303211",
            "provider" : "MTN"
    }
    })
    headers = {
        'Authorization': f'Bearer {PAYSTACK_SECRET_KEY}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
# mobile_money_transaction()



def send_otp():

    url = "https://api.paystack.co/charge/submit_otp"

    payload='otp=123456&reference=5bwib5v6anhe9xa'
    headers = {
        'Authorization': f'Bearer {PAYSTACK_SECRET_KEY}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

# send_otp()
