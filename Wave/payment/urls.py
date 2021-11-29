from django.urls import path
from .views import form, flutterwave_initiate_payment

urlpatterns = [
    # path('home', form, name='home'),
    path('', flutterwave_initiate_payment, name='initiate'),
    path('payment/success/', flutterwave_initiate_payment, name='success'),
]
