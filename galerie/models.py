from django.db import models

class Photo(models.Model):
    titre = models.CharField(max_length=200)
    image = models.ImageField(upload_to='galerie/photos/')
    evenement = models.CharField(max_length=200, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Video(models.Model):
    titre = models.CharField(max_length=200)
    youtube_id = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titre
