from django.urls import path
from .views import MemebershipSelectView

urlpatterns=[
    path('membership/',MemebershipSelectView.as_view(), name='membership' )
]