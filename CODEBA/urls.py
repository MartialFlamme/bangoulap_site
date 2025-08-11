from django.urls import path
from . import views

app_name = 'education'

urlpatterns = [
    path('presentation/', views.presentation_du_CODEBA, name='presentation_du_CODEBA'),
    path('activite/', views.activite_du_CODEBA, name='activite_du_CODEBA'),
]
