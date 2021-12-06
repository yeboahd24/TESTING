from django.urls import path
from .views import vgs_view, flutterwave_initiate_payment

urlpatterns = [
    # path('home', form, name='home'),
    path('', flutterwave_initiate_payment, name='initiate'),
    path('payment/success/', flutterwave_initiate_payment, name='success'),
    path('vgs/', vgs_view, name='vgs'),
]
