# dons/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import DonForm
from .models import Don

def formulaire_don(request):
    if request.method == 'POST':
        form = DonForm(request.POST)
        if form.is_valid():
            don = form.save()

            html_message = render_to_string('dons/email_confirmation.html', {'don': don})
            email = EmailMessage(
                subject=f"✅ Nouveau Don Reçu de {don.nom}",
                body=html_message,
                from_email=settings.EMAIL_HOST_USER,
                to=['ketchadjiguymartial@gmail.com'],
                reply_to=[don.email],
            )
            email.content_subtype = 'html'
            email.send()

            return redirect('dons:confirmation', don_id=don.id)
    else:
        form = DonForm()

    return render(request, 'dons/formulaire_don.html', {'form': form})

def confirmation_don(request, don_id):
    don = get_object_or_404(Don, id=don_id)
    return render(request, 'dons/confirmation_don.html', {'don': don, 'email_envoye': True})


