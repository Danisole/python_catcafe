from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    content = forms.CharField(labeñ="", widget=forms.Textarea(attrs={}))