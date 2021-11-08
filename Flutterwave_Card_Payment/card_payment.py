from json import JSONEncoder
import pickle
import requests
import os
import pin
import encryption
import json


class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (list, dict, str, unicode, int, float, bool, type(None))):
            return JSONEncoder.default(self, obj)
        return {'_python_object': pickle.dumps(obj)}


def flutterwave_card_payment(amount, card_number, expiry_year, expiry_month, cvv, pin):
    """
    This function will make a card payment to a flutterwave account
    """

    # import the necessary variables
    url = os.environ.get('FLUTTERWAVE_URL')
    secret_key = os.environ.get('FLUTTERWAVE_SECRET_KEY')
    public_key = os.environ.get('FLUTTERWAVE_PUBLIC_KEY')
    # create the headers
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + secret_key
    }
    # create the data
    data = {
        'amount': amount,
        'card_number': card_number,
        'cvv': cvv,
        'expiry_month': expiry_month,
        'expiry_year': expiry_year,
        'currency': 'GHS',
        'country': 'GH',
        'email': 'dominic@gmail.com',
        'phone_number': '0540303211',
        'tx_ref': 'hooli-tx-1920bbtytty',
        "authorization": {
            "mode": "pin",
            "pin": pin,
        }
    }

    data = PythonObjectEncoder().encode(data)
    hashed_sec_key = encryption.PayTest.getKey(secret_key)
    encrypt_3DES_key = encryption.PayTest.encryptData(hashed_sec_key, data)

    # payment payload
    payload = {
        "PBFPubKey": public_key,
        "client": encrypt_3DES_key,
        "alg": "3DES-24"
    }
    payload = PythonObjectEncoder().encode(payload)
    # make the request
    response = requests.post(url, headers=headers, data=payload)
    return response.json()
    # return PythonObjectEncoder(response) if response.status_code == 200 else response.json()


pay = flutterwave_card_payment(
    amount=100, card_number='5531886652142950', expiry_month='03',
    expiry_year='24', cvv='564', pin='3310')
print(pay)





def flutterwave_mobile_money_payment(amount, phone_number, pin):
    """
    This function will make a mobile money payment to a flutterwave account
    """

    # import the necessary variables
    url = os.environ.get('FLUTTERWAVE_URL')
    secret_key = os.environ.get('FLUTTERWAVE_SECRET_KEY')
    public_key = os.environ.get('FLUTTERWAVE_PUBLIC_KEY')
    # create the headers
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + secret_key
    }
    # create the data
    data = {
        'amount': amount,
        'currency': 'GHS',
        'country': 'GH',
        'email': ''
    }
    data = PythonObjectEncoder().encode(data)
    hashed_sec_key = encryption.PayTest.getKey(secret_key)
    encrypt_3DES_key = encryption.PayTest.encryptData(hashed_sec_key, data)
    
    # payment payload
    payload = {
        "PBFPubKey": public_key,
        "client": encrypt_3DES_key,
        "alg": "3DES-24"
    }
    payload = PythonObjectEncoder().encode(payload)
    # make the request
    response = requests.post(url, headers=headers, data=payload)
    return response.json()


mobile = flutterwave_mobile_money_payment(
    amount=100, phone_number='0540303211', pin='3310')
print(mobile)
