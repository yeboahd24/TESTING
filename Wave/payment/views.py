from django.shortcuts import render, redirect
from django.conf import settings
from .forms import PaymentForm
from django.http import HttpResponse
import requests
from .models import Payment
from django.core.mail import send_mail
import random

headers = {
    'Authorization': 'Bearer ' + settings.FLUTTERWAVE_SECRET_KEY,
    'Content-Type': 'application/json'
}
url = 'https://api.flutterwave.com/v3/payments'


def form(request):
    return render(request, 'forms.html')


def flutterwave_initiate_payment(request):

    if request.method == 'POST':

        data = {
            "tx_ref": f"hooli-tx-{random.randrange(1, 10000)}bbtytty",
            "currency": "GHS",
            "amount": request.POST.get('amount'),

            "redirect_url": "http://127.0.0.1:8000",
            "payment_options": "card",

            "customer": {
                "email": request.POST.get('email'),
                "phonenumber": "08088884528",
                "name": request.POST.get('name'),
            },
        }
        response = requests.post(url, json=data, headers=headers)
        print(response.json())
        send_mail(
            'Payment Link',
            'Your payment has been initiated. Please open this link to make your payment ' + response.json()['data']['link'],
            
            request.POST.get('email'),['yeboahd24@gmail.com'],
            fail_silently=False,
        )
        return HttpResponse('Payment has been initiated, Please check your email for further process')
            
    return render(request, 'payment.html')


