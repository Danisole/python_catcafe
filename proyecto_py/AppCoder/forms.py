from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SuscriptorForm(forms.Form):

    nombre=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nombre...'}))
    apellido=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Apellido...'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email...'}))

class ComentariosForm(forms.Form):

    nombre=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nombre...'}))
    reseña=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder': 'Reseña en 140 caracteres'}))
    estrellas=forms.IntegerField(min_value=1, max_value=5)  

class RegistroUsuarioForm(UserCreationForm):
    email=forms.EmailField(label="Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}


