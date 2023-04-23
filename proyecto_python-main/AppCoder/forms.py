from django import forms

class SuscriptorForm(forms.Form):

    nombre=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nombre...'}))
    apellido=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Apellido...'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email...'}))

class ComentariosForm(forms.Form):

    nombre=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nombre...'}))
    reseña=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder': 'Reseña en 140 caracteres'}))
    estrellas=forms.IntegerField(min_value=1, max_value=5)  


