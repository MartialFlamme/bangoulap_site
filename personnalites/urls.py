from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "personnalites"

urlpatterns = [
    # ✅ ROUTES ADMIN en premier !
    path('admin/', views.admin_liste_personnalites, name='admin_liste'),
    path('admin/ajouter/', views.ajouter_personnalite, name='ajouter'),
    path('admin/modifier/<int:pk>/', views.modifier_personnalite, name='modifier'),
    path('admin/supprimer/<int:pk>/', views.supprimer_personnalite, name='supprimer'),

    # ✅ ROUTES PUBLIQUES ensuite
    path('', views.liste_personnalites, name='liste'),
    path('<slug:slug>/', views.detail_personnalite, name='detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)