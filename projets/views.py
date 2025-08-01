# projets/views.py
from django.shortcuts import redirect, render, get_object_or_404
from .models import Projet
from django.contrib.auth.decorators import user_passes_test
from .forms import ProjetForm

def liste_projets(request):
    projets = Projet.objects.all().order_by('-date_lancement')
    return render(request, 'projets/liste_projets.html', {'projets': projets})

def detail_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    return render(request, 'projets/detail_projet.html', {'projet': projet})

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def admin_liste_projets(request):
    projets = Projet.objects.all().order_by('-date_lancement')
    return render(request, 'projets/admin/liste.html', {'projets': projets})

@user_passes_test(is_superuser)
def ajouter_projet(request):
    form = ProjetForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('projets:admin_liste')
    return render(request, 'projets/admin/form.html', {'form': form, 'titre': "Ajouter un projet"})

@user_passes_test(is_superuser)
def modifier_projet(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    form = ProjetForm(request.POST or None, request.FILES or None, instance=projet)
    if form.is_valid():
        form.save()
        return redirect('projets:admin_liste')
    return render(request, 'projets/admin/form.html', {'form': form, 'titre': "Modifier le projet"})

@user_passes_test(is_superuser)
def supprimer_projet(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    if request.method == 'POST':
        projet.delete()
        return redirect('projets:admin_liste')
    return render(request, 'projets/admin/confirm_delete.html', {'objet': projet})