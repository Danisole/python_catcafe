from django.urls import path
from .views import *

urlpatterns =[
    path("", feed, name='feed'),
    path('profile/', profile, name='profile'),
]