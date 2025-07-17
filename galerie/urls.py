from django.urls import path
from . import views

app_name = 'galerie'

urlpatterns = [
    path('photos/', views.galerie_photos, name='photos'),
    path('videos/', views.galerie_videos, name='videos'),
]
