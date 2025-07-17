from django.urls import path
from . import views

app_name = 'education'

urlpatterns = [
    path('projets/', views.projets_educatifs, name='projets_educatifs'),
    path('academie-hoteliere/', views.academie_hoteliere, name='academie_hoteliere'),
]
