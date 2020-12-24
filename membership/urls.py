from django.urls import path
from .views import MemebershipSelectView


urlpatterns =[
    path('', MemebershipSelectView.as_view(),name='membership')]