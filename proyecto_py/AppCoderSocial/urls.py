from django.urls import path
from .views import *


urlpatterns =[
    path("feed/", feed, name='feed'),
    path('profile/', profile, name='profile'),
    path('profile/<str:username>/', profile, name='profile'),
    path('post/', post, name='post'),
    path('follow/<str:username>/', follow, name='follow'),
    path('unfollow/<str:username>/', unfollow, name='unfollow'),

]  
