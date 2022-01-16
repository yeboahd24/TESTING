from json import JSONEncoder
import pickle
import requests
import os
import pin
import encryption



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
        'Authorization': 'Bearer ' + secret_key,
        'Cache-Control': 'no-cache',
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
        'redirect_url': 'https://webhook.site/c1ff1154-8535-4d1a-99a6-5b32cc5c366d',
        'email': 'yeboahd24@gmail.com',
        'phone_number': '0540303211',
        "preauthorize": True,
        'tx_ref': "MC-3243e",
        "authorization": {
            "mode": "pin",
            "pin": pin,

        },
    }

    data = PythonObjectEncoder().encode(data)
    hashed_sec_key = encryption.PayTest.getKey(secret_key)
    encrypt_3DES_key = encryption.PayTest.encryptData(hashed_sec_key, data)
    # print(encrypt_3DES_key)

    # payment payload
    payload = {
        "PBFPubKey": public_key,
        "client": encrypt_3DES_key,
        "alg": "3DES-24",
    }
    payload = PythonObjectEncoder().encode(payload)

    # make the request
    response = requests.post(url, headers=headers, data=payload)
    return response.json()


if __name__ == '__main__':
    pay = flutterwave_card_payment(
        amount=100, card_number='5531886652142950', expiry_month='09',
        expiry_year='34', cvv='564', pin='3310')
    print(pay)