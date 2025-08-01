from django.urls import path
from . import views

app_name = 'galerie'

urlpatterns = [
        # 🔧 CRUD PHOTOS
    path('admin/photos/', views.admin_photos, name='admin_photos'),
    path('admin/photos/ajouter/', views.ajouter_photo, name='ajouter_photo'),
    path('admin/photos/modifier/<int:pk>/', views.modifier_photo, name='modifier_photo'),
    path('admin/photos/supprimer/<int:pk>/', views.supprimer_photo, name='supprimer_photo'),

    # 🔧 CRUD VIDEOS
    path('admin/videos/', views.admin_videos, name='admin_videos'),
    path('admin/videos/ajouter/', views.ajouter_video, name='ajouter_video'),
    path('admin/videos/modifier/<int:pk>/', views.modifier_video, name='modifier_video'),
    path('admin/videos/supprimer/<int:pk>/', views.supprimer_video, name='supprimer_video'),
    path('photos/', views.galerie_photos, name='photos'),
    path('videos/', views.galerie_videos, name='videos'),
]
