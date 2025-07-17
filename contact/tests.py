from django.test import TestCase
from .forms import ContactForm

class ContactFormTest(TestCase):
    def test_form_valid(self):
        form_data = {
            'nom': 'Marie',
            'email': 'marie@example.com',
            'message': 'Bonjour, je soutiens le projet !'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
