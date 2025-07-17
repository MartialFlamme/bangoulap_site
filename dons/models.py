# dons/models.py
from django.db import models
from projets.models import Projet

class Don(models.Model):
    MOYENS_PAIEMENT = (
        ('momo', 'Mobile Money'),
        ('om', 'Orange Money'),
    )

    nom = models.CharField(max_length=100)
    email = models.EmailField()
    numero = models.CharField(max_length=20)
    montant = models.PositiveIntegerField()
    moyen = models.CharField(max_length=10, choices=MOYENS_PAIEMENT)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='dons')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.montant} FCFA"
