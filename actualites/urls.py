from django.urls import path
from . import views

app_name = 'actualites'

urlpatterns = [
    path('', views.liste_actualites, name='liste'),
    path('article/<slug:slug>/', views.detail_actualite, name='detail'),
    path('calendrier/', views.calendrier_evenements, name='calendrier'),
]
