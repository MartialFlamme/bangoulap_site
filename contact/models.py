from django.db import models

class MessageContact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} ({self.email})"

class ContenuPropose(models.Model):
    nom = models.CharField(max_length=100)
    type_contenu = models.CharField(max_length=50, choices=[
        ('evenement', 'Événement'),
        ('texte', 'Texte'),
        ('photo', 'Photo'),
        ('autre', 'Autre')
    ])
    contenu = models.TextField()
    date_proposition = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.type_contenu}"
