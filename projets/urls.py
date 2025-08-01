from django.urls import path
from . import views

app_name = 'projets'

urlpatterns = [
    path('', views.liste_projets, name='liste_projets'),
    path('detail/<int:projet_id>/', views.detail_projet, name='detail'),
        # 🔧 CRUD admin
    path('admin/', views.admin_liste_projets, name='admin_liste'),
    path('admin/ajouter/', views.ajouter_projet, name='ajouter'),
    path('admin/modifier/<int:pk>/', views.modifier_projet, name='modifier'),
    path('admin/supprimer/<int:pk>/', views.supprimer_projet, name='supprimer'),
]
