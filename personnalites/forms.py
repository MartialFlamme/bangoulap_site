from django import forms
from .models import Personnalite

class PersonnaliteForm(forms.ModelForm):
    class Meta:
        model = Personnalite
        fields = ['nom', 'slug', 'photo', 'fonction', 'biographie']
