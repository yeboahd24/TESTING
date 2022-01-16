from django.urls import path
from .views import vgs_view, flutterwave_initiate_payment, music_results, music

urlpatterns = [
    # path('home', form, name='home'),
    path('', flutterwave_initiate_payment, name='initiate'),
    path('payment/success/', flutterwave_initiate_payment, name='success'),
    path('vgs/', vgs_view, name='vgs'),
    path('results/', music_results, name='music'),
    path('music/', music, name='music'),
]
