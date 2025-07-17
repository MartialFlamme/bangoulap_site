# projets/views.py
from django.shortcuts import render, get_object_or_404
from .models import Projet

def liste_projets(request):
    projets = Projet.objects.all().order_by('-date_lancement')
    return render(request, 'projets/liste_projets.html', {'projets': projets})

def detail_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    return render(request, 'projets/detail_projet.html', {'projet': projet})

