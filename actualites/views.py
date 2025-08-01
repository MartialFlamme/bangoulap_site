from django.shortcuts import redirect, render, get_object_or_404
from .models import Actualite
from django.contrib.auth.decorators import user_passes_test
from .forms import ActualiteForm
from django.utils.text import slugify


def liste_actualites(request):
    actualites = Actualite.objects.filter(publie=True).order_by('-date')
    return render(request, 'actualites/liste_actualites.html', {'actualites': actualites})

def detail_actualite(request, slug):
    actualite = get_object_or_404(Actualite, slug=slug)
    return render(request, 'actualites/detail_actualite.html', {'actualite': actualite})

def calendrier_evenements(request):
    evenements = Actualite.objects.filter(publie=True).order_by('date')
    return render(request, 'actualites/calendrier.html', {'evenements': evenements})

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def admin_liste_actualites(request):
    actualites = Actualite.objects.all().order_by('-date')
    return render(request, 'actualites/admin/liste.html', {'actualites': actualites})

@user_passes_test(is_superuser)
def ajouter_actualite(request):
    form = ActualiteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        actualite = form.save(commit=False)
        actualite.slug = slugify(actualite.titre)
        actualite.save()
        return redirect('actualites:admin_liste')
    return render(request, 'actualites/admin/form.html', {'form': form, 'titre': "Ajouter une actualité"})

@user_passes_test(is_superuser)
def modifier_actualite(request, pk):
    actualite = get_object_or_404(Actualite, pk=pk)
    form = ActualiteForm(request.POST or None, request.FILES or None, instance=actualite)
    if form.is_valid():
        form.save()
        return redirect('actualites:admin_liste')
    return render(request, 'actualites/admin/form.html', {'form': form, 'titre': "Modifier l'actualité"})

@user_passes_test(is_superuser)
def supprimer_actualite(request, pk):
    actualite = get_object_or_404(Actualite, pk=pk)
    if request.method == 'POST':
        actualite.delete()
        return redirect('actualites:admin_liste')
    return render(request, 'actualites/admin/confirm_delete.html', {'objet': actualite})