from django.urls import path
from . import views

app_name = 'dons'

urlpatterns = [
    path('formulaire/', views.formulaire_don, name='formulaire'),
    path('confirmation/<int:don_id>/', views.confirmation_don, name='confirmation'),
]
