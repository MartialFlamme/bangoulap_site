from django.urls import path
from . import views

app_name = 'projets'

urlpatterns = [
    path('', views.liste_projets, name='liste_projets'),
    path('detail/<int:projet_id>/', views.detail_projet, name='detail'),
]
