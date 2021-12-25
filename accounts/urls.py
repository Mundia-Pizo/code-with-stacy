from django.urls import path
from .views import RegistrationView, profile

urlpatterns=[
    path('register', RegistrationView.as_view(), name='register'),
    path('my-profile', profile, name='profile')
]