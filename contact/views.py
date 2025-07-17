from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Construction du message complet
            full_message = (
                f"📬 Nouveau message de {nom}\n\n"
                f"📧 Adresse email : {email}\n\n"
                f"💬 Message :\n{message}"
            )

            email_message = EmailMessage(
                subject="📩 Message de contact depuis le site de Bangoulap",
                body=full_message,
                from_email=settings.EMAIL_HOST_USER,  # adresse technique
                to=['ketchadjiguymartial@gmail.com'],
                reply_to=[email]  # Ajouter l'adresse de l'expéditeur pour pouvoir y répondre directement
            )
            email_message.send(fail_silently=False)
            sent = True
            form = ContactForm()  # Réinitialise le formulaire pour vider les champs
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form, 'sent': sent})
