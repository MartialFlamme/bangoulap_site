from django.db import models

class Personnalite(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default='inconnu')
    photo = models.ImageField(upload_to='personnalites/')
    fonction = models.CharField(max_length=150)
    biographie = models.TextField()

    def __str__(self):
        return self.nom
