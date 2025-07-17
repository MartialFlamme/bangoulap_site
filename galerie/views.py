from django.shortcuts import render
from .models import Photo, Video

def galerie_photos(request):
    photos = Photo.objects.all()
    return render(request, 'galerie/photos.html', {'photos': photos})

def galerie_videos(request):
    videos = Video.objects.all()
    return render(request, 'galerie/videos.html', {'videos': videos})
