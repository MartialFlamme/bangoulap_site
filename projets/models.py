# projets/models.py
from django.db import models

class Projet(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_lancement = models.DateField()
    image = models.ImageField(upload_to='projets/images/', blank=True, null=True)

    def __str__(self):
        return self.titre
