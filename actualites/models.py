from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Actualite(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='actualites/', default='images/default.jpg')  # 👈 ajoute default ici
    contenu = models.TextField()
    date = models.DateField(default=timezone.now)
    publie = models.BooleanField(default=False)
