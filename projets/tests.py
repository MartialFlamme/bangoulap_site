from django.test import TestCase
from .models import Projet

class ProjetModelTest(TestCase):
    def test_projet_str(self):
        p = Projet.objects.create(
            titre="Projet Test",
            description="Description",
            etat="en_cours",
            partenaires="CODEBA",
            image="projets/test.jpg"
        )
        self.assertEqual(str(p), "Projet Test")
