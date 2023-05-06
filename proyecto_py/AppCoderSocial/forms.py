from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'row':2, 'placeholder': '¿Que estas pensando?'}), required=True)

    class Meta:
        model = Post
        fields = ['content']

