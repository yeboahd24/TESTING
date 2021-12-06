import requests
import pin
import os

FLUTTERWAVE_SECRET_KEY = os.environ.get('FLUTTERWAVE_SECRET_KEY')


def verify_payment(reference, *args, **kwargs):
    verification_url = f'https://api.flutterwave.com/v3/transactions/{reference}/verify'

    headers = {
         "Content-Type": "application/json",
          "Authorization": "Bearer " + FLUTTERWAVE_SECRET_KEY
         }

    url = verification_url
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        return response_data['status'], response_data['data']
    response_data = response.json()
    return response_data['status'], response_data['message']


if __name__ == '__main__':
    flutterwave = verify_payment()
