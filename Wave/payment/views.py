from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
import requests
from django.core.mail import send_mail
import random
import asyncio
import httpx


headers = {
    'Authorization': 'Bearer ' + settings.FLUTTERWAVE_SECRET_KEY,
    'Content-Type': 'application/json'
}
url = 'https://api.flutterwave.com/v3/payments'


def form(request):
    return render(request, 'forms.html')


async def flutterwave_initiate_payment(request):

    if request.method == 'POST':

        data = {
            "tx_ref": f"hooli-tx-{random.randrange(1, 10000)}bbtytty",
            "currency": "GHS",
            "amount": request.POST.get('amount'),

            "redirect_url": request.build_absolute_uri('/payment/success/'),
            "payment_options": "card",

            "customer": {
                "email": request.POST.get('email'),
                "phonenumber": "08088884528",
                "name": request.POST.get('name'),
            },
        }
        # response = httpx.post(url, json=data, headers=headers)
        # print(response.json())
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data, headers=headers)
            print(response.json())
        # return redirect(response.json()['data']['authorization_url'])
            send_mail(
                'Payment Link',
                'Your payment has been initiated. Please open this link to make your payment ' +
                response.json()['data']['link'],

                request.POST.get('email'), ['yeboahd24@gmail.com'],
                fail_silently=False,
            )
            return HttpResponse('Payment has been initiated, Please check your email for further process')

    return render(request, 'payment.html')


def vgs_view(request):
    if request.method == 'POST':
        return render(request, 'vgs.html')
    return render(request, 'vgs.html')


