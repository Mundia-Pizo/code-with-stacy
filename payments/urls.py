from django.urls import path
from .views import Payments, PaymentSuccess

urlpatterns=[
    path('payment/',Payments.as_view(), name='payment' ), 
    path('success/', PaymentSuccess.as_view(), name='success')
]