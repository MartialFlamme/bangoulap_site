from django.shortcuts import render, get_object_or_404
from .models import Personnalite

def liste_personnalites(request):
    personnalites = Personnalite.objects.all()
    return render(request, 'personnalites/liste_personnalites.html', {'personnalites': personnalites})

def detail_personnalite(request, slug):
    personne = get_object_or_404(Personnalite, slug=slug)
    return render(request, 'personnalites/detail_personnalite.html', {'personne': personne})
