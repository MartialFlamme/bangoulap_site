from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# ✅ Formulaire de connexion personnalisé
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nom d’utilisateur'
        })
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mot de passe'
        })
    )

# ✅ Création utilisateur
class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Mot de passe")
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff', 'is_superuser', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

# ✅ Modification utilisateur
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff', 'is_superuser']
