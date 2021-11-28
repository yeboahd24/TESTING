import requests

VGS_URL = "https://echo.apps.verygood.systems/post"

USERNAME = "maryyeboah70@tnttukbbvmi.sandbox.verygoodproxy.com:8080" 


def flutterwave_direct_charge_api_with_very_good_security():
    """
    This function is used to make a direct charge request to the flutterwave payment gateway using the very good security proxy
    """
    data = {
        "amount": "100",
        "currency": "NGN",
        "email": ""
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer " + USERNAME
    }
    
    