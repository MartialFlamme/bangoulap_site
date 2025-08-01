from django.urls import path
from . import views

app_name = 'actualites'

urlpatterns = [
    path('', views.liste_actualites, name='liste'),
    path('article/<slug:slug>/', views.detail_actualite, name='detail'),
    path('calendrier/', views.calendrier_evenements, name='calendrier'),
        # Routes admin
    path('admin/', views.admin_liste_actualites, name='admin_liste'),
    path('admin/ajouter/', views.ajouter_actualite, name='ajouter'),
    path('admin/modifier/<int:pk>/', views.modifier_actualite, name='modifier'),
    path('admin/supprimer/<int:pk>/', views.supprimer_actualite, name='supprimer'),
]
