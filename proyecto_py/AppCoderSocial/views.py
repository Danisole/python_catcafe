from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import *
from AppCoder.models import * 
from AppCoder.views import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def feed(request):
    posts = Post.objects.all()

    context = {'posts': posts, "avatar": obtenerAvatar(request)}
    return render(request, 'AppCoderSocial/feed.html', context)


@login_required
def profile(request, username=None):
    current_user = request.user
    if username and username !=  current_user. username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user

    return render(request, 'AppCoderSocial/profile.html', {"user": user, "posts": posts, "avatar": obtenerAvatar(request)})


@login_required
def post(request):
    current_user=get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post enviado')
            return redirect('feed')
    else: 
        form = PostForm()
    return render(request, 'AppCoderSocial/post.html', {'form': form, "avatar": obtenerAvatar(request)})


@login_required
def follow(request, username):
    current_user =request.user
    to_user =User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    messages.success(request, f'Sigues a {username}')
    return redirect('feed')


@login_required
def unfollow(request, username):
    current_user =request.user
    to_user =User.objects.get(username=username)
    to_user_id = to_user.id 
    rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    messages.success(request, f'Ya no sigues a {username}')
    return redirect('feed')

