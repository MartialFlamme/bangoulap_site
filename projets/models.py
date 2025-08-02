# projets/models.py
from django.db import models

class Projet(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_lancement = models.DateField(verbose_name="Date de lancement", blank=True, null=True)
    image = models.ImageField(upload_to='projets/images/', blank=True, null=True)

    def __str__(self):
        return self.titre
