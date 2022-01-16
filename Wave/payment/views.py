from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
import requests
from django.core.mail import send_mail
import random
import httpx
from .models import Music


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


def music_results(request):

    musics = get_object_or_404(Music)

    url = "https://shazam.p.rapidapi.com/songs/list-artist-top-tracks"

    querystring = {"id":"40008598","locale":"en-US"}

    headers = {
        'x-rapidapi-host': "shazam.p.rapidapi.com",
        'x-rapidapi-key': "f0e9484262mshfd3c258499e71b9p109e6djsnf8c3614c3590"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return HttpResponse(response.text)
    # tracks = response.json()['tracks']
    # for track in tracks:
    #     musics.title = track['title']
    #     musics.link = track['share']['link']
    #     musics.image = track['share']['image']
    #     musics.save()
    #     # print(track['title'])
    #     # print(track['share']['href'])
    #     # print(track['share']['image'])
    # return render(request, 'index.html', {'musics': musics})

def music(request):
    musics = Music.objects.all()

    url = "https://shazam.p.rapidapi.com/songs/list-artist-top-tracks"

    querystring = {"id":"40008598","locale":"en-US"}

    headers = {
        'x-rapidapi-host': "shazam.p.rapidapi.com",
        'x-rapidapi-key': "f0e9484262mshfd3c258499e71b9p109e6djsnf8c3614c3590"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    tracks = response.json()['tracks']
    for track in tracks:
        musics.title = track['title']
        musics.link = track['share']['href']
        musics.image = track['share']['image']
        musics.save()
    return render(request, 'index.html', {'musics': musics})
