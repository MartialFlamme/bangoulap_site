from django.db import models

class ProjetEducatif(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.titre

class AcademieHoteliere(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='education/academie/')

    def __str__(self):
        return self.nom
