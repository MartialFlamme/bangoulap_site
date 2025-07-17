# dons/forms.py
from django import forms
from .models import Don
from projets.models import Projet

class DonForm(forms.ModelForm):
    class Meta:
        model = Don
        fields = ['nom', 'email', 'numero', 'montant', 'moyen', 'projet']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Affiche les projets dans l’ordre alphabétique
        self.fields['projet'].queryset = Projet.objects.order_by('titre')
        self.fields['projet'].label = "Projet soutenu"
