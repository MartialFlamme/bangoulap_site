from django.test import TestCase
from .models import Actualite

class ActualiteModelTest(TestCase):
    def test_creation_actualite(self):
        actualite = Actualite.objects.create(
            titre="Test Actu",
            contenu="Contenu test",
            auteur="Admin",
            publie=True
        )
        self.assertEqual(actualite.__str__(), "Test Actu")
        self.assertTrue(actualite.publie)
