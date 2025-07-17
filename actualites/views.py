from django.shortcuts import render, get_object_or_404
from .models import Actualite

def liste_actualites(request):
    actualites = Actualite.objects.filter(publie=True).order_by('-date')
    return render(request, 'actualites/liste_actualites.html', {'actualites': actualites})

def detail_actualite(request, slug):
    actualite = get_object_or_404(Actualite, slug=slug)
    return render(request, 'actualites/detail_actualite.html', {'actualite': actualite})

def calendrier_evenements(request):
    evenements = Actualite.objects.filter(publie=True).order_by('date')
    return render(request, 'actualites/calendrier.html', {'evenements': evenements})
