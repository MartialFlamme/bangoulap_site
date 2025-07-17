from django.test import TestCase
from .models import Don

class DonModelTest(TestCase):
    def test_don_creation(self):
        don = Don.objects.create(
            nom="Jean Test",
            email="jean@example.com",
            montant=10000,
            moyen='momo'
        )
        self.assertEqual(don.montant, 10000)
        self.assertEqual(don.moyen, 'momo')
