from django.shortcuts import render
from django.db import models
from .models import *

# Create your views here.
def feed(request):
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'AppCoderSocial/feed.html', context)

def profile(request):
    return render(request, 'AppCoderSocial/profile.html')

