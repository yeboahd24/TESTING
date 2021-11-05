import secret
import json
import requests
import os


SECRET_KEY = os.environ.get('YOCO_TEST_SECRET_KEY')

def charge_user():
    response = requests.post(
        'https://online.yoco.com/v1/charges/',
        headers={
            'X-Auth-Secret-Key': SECRET_KEY,
        },
        json={
            'token': 'tok_test_DjaqoUgmzwYkwesr3euMxyUV4g',
            'amountInCents': 2799,
            'currency': 'ZAR',
        },
        )

# charge_user()


def charge_by_card():
    base_url = ''