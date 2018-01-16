from django import forms

from .models import Post
from .models import Lekarz

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class LekarzForm(forms.ModelForm):

    class Meta:
        model = Lekarz
        fields = ('nazwisko', 'imię', 'specjalizacja', 'cena', 'opis',)