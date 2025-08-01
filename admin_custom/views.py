from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.utils import timezone
from django.db.models import Sum
from django.template import loader
from django.urls import reverse

from .forms import CustomLoginForm, UserCreateForm, UserUpdateForm

# Import des modèles utilisés dans le tableau de bord
from dons.models import Don
from actualites.models import Actualite
from galerie.models import Photo, Video
from personnalites.models import Personnalite


# ✅ Vue de connexion personnalisée
def custom_login(request):
    if request.user.is_authenticated:
        return redirect(reverse("admin_custom:dashboard"))

    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse("admin_custom:dashboard") + "?welcome=1")
    else:
        form = CustomLoginForm()

    return render(request, "admin-custom/login.html", {"form": form})


# ✅ Vue de déconnexion
@login_required
def custom_logout(request):
    logout(request)
    return redirect("/?logged_out=1")


# ✅ Tableau de bord (réservé aux utilisateurs staff)
@login_required
def dashboard(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Accès refusé.")

    total_actualites = Actualite.objects.count()
    total_dons = Don.objects.count()
    total_montant = Don.objects.aggregate(Sum("montant"))["montant__sum"] or 0
    total_photos = Photo.objects.count()
    total_videos = Video.objects.count()
    total_personnalites = Personnalite.objects.count()

    six_mois = timezone.now() - timezone.timedelta(days=180)
    dons_recents = (
        Don.objects.filter(created_at__gte=six_mois)
        .extra(select={'month': "strftime('%%m', created_at)"})
        .values('month')
        .annotate(total=Sum('montant'))
        .order_by('month')
    )

    labels = [f"Mois {mois['month']}" for mois in dons_recents]
    dons_par_mois = [mois["total"] for mois in dons_recents]

    derniers_dons = Don.objects.select_related("projet").order_by("-created_at")[:10]
    dernieres_actualites = Actualite.objects.order_by("-date")[:6]

    return render(request, "admin-custom/dashboard.html", {
        "total_actualites": total_actualites,
        "total_dons": total_dons,
        "total_montant": total_montant,
        "total_photos": total_photos,
        "total_videos": total_videos,
        "total_personnalites": total_personnalites,
        "labels": labels,
        "dons_par_mois": dons_par_mois,
        "derniers_dons": derniers_dons,
        "dernieres_actualites": dernieres_actualites,
    })


# ✅ Gestion des utilisateurs
@permission_required("auth.view_user")
def user_list(request):
    query = request.GET.get("q", "")
    users = User.objects.filter(username__icontains=query) if query else User.objects.all()
    return render(request, "admin-custom/users/list.html", {"users": users, "query": query})


@permission_required("auth.add_user")
def user_create(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin_custom:user_list")
    else:
        form = UserCreateForm()
    return render(request, "admin-custom/users/create.html", {"form": form})


@permission_required("auth.change_user")
def user_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("admin_custom:user_list")
    else:
        form = UserUpdateForm(instance=user)
    return render(request, "admin-custom/users/edit.html", {"form": form, "user": user})


@permission_required("auth.delete_user")
def user_delete(request, user_id):
    if request.method == "POST":
        user = get_object_or_404(User, id=user_id)
        if user != request.user:  # Empêche la suppression de soi-même
            user.delete()
    return redirect("admin_custom:user_list")


# ✅ Vue personnalisée pour les erreurs CSRF 403
def custom_permission_denied_view(request, exception=None, reason=""):
    template = loader.get_template("admin-custom/403.html")
    context = {"reason": reason}
    return HttpResponseForbidden(template.render(context, request))
