from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Personnalite
from .forms import PersonnaliteForm

# 🌍 Liste publique
def liste_personnalites(request):
    personnalites = Personnalite.objects.all()
    return render(request, 'personnalites/liste_personnalites.html', {'personnalites': personnalites})

# 🌍 Détail public
def detail_personnalite(request, slug):
    personne = get_object_or_404(Personnalite, slug=slug)
    return render(request, 'personnalites/detail_personnalite.html', {'personne': personne})

# ✅ Accès admin uniquement
def is_superuser(user):
    return user.is_superuser

# 🔧 Liste admin
@user_passes_test(is_superuser)
def admin_liste_personnalites(request):
    personnalites = Personnalite.objects.all()
    return render(request, 'personnalites/admin/liste.html', {'personnalites': personnalites})

# 🔧 Ajouter
@user_passes_test(is_superuser)
def ajouter_personnalite(request):
    form = PersonnaliteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('personnalites:admin_liste')
    return render(request, 'personnalites/admin/form.html', {
        'form': form,
        'titre': "Ajouter une personnalité"
    })

# 🔧 Modifier
@user_passes_test(is_superuser)
def modifier_personnalite(request, pk):
    p = get_object_or_404(Personnalite, pk=pk)
    form = PersonnaliteForm(request.POST or None, request.FILES or None, instance=p)
    if form.is_valid():
        form.save()
        return redirect('personnalites:admin_liste')
    return render(request, 'personnalites/admin/form.html', {
        'form': form,
        'titre': "Modifier la personnalité"
    })

# 🔧 Supprimer
@user_passes_test(is_superuser)
def supprimer_personnalite(request, pk):
    p = get_object_or_404(Personnalite, pk=pk)
    if request.method == 'POST':
        p.delete()
        return redirect('personnalites:admin_liste')
    return render(request, 'personnalites/admin/confirm_delete.html', {'objet': p})
