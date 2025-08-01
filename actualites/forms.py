from django import forms
from .models import Actualite

class ActualiteForm(forms.ModelForm):
    class Meta:
        model = Actualite
        fields = ['titre', 'auteur', 'image', 'contenu', 'date', 'publie']
