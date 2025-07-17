from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(label='Nom', max_length=100, widget=forms.TextInput(attrs={
        'class': 'w-full p-2 border rounded',
        'placeholder': 'Votre nom'
    }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'w-full p-2 border rounded',
        'placeholder': 'Votre email'
    }))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={
        'class': 'w-full p-2 border rounded',
        'placeholder': 'Votre message...'
    }))
