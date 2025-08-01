from django.shortcuts import get_object_or_404, redirect, render
from .models import Photo, Video
from django.contrib.auth.decorators import user_passes_test
from .forms import PhotoForm, VideoForm

def galerie_photos(request):
    photos = Photo.objects.all()
    return render(request, 'galerie/photos.html', {'photos': photos})

def galerie_videos(request):
    videos = Video.objects.all()
    return render(request, 'galerie/videos.html', {'videos': videos})

def is_superuser(user):
    return user.is_superuser

# PHOTOS
@user_passes_test(is_superuser)
def admin_photos(request):
    photos = Photo.objects.all().order_by('-date')
    return render(request, 'galerie/admin/photos_liste.html', {'photos': photos})

@user_passes_test(is_superuser)
def ajouter_photo(request):
    form = PhotoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('galerie:admin_photos')
    return render(request, 'galerie/admin/photo_form.html', {'form': form, 'titre': "Ajouter une photo"})

@user_passes_test(is_superuser)
def modifier_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    form = PhotoForm(request.POST or None, request.FILES or None, instance=photo)
    if form.is_valid():
        form.save()
        return redirect('galerie:admin_photos')
    return render(request, 'galerie/admin/photo_form.html', {'form': form, 'titre': "Modifier la photo"})

@user_passes_test(is_superuser)
def supprimer_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        photo.delete()
        return redirect('galerie:admin_photos')
    return render(request, 'galerie/admin/confirm_delete.html', {'objet': photo})


# VIDEOS
@user_passes_test(is_superuser)
def admin_videos(request):
    videos = Video.objects.all().order_by('-date')
    return render(request, 'galerie/admin/videos_liste.html', {'videos': videos})

@user_passes_test(is_superuser)
def ajouter_video(request):
    form = VideoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('galerie:admin_videos')
    return render(request, 'galerie/admin/video_form.html', {'form': form, 'titre': "Ajouter une vidéo"})

@user_passes_test(is_superuser)
def modifier_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    form = VideoForm(request.POST or None, instance=video)
    if form.is_valid():
        form.save()
        return redirect('galerie:admin_videos')
    return render(request, 'galerie/admin/video_form.html', {'form': form, 'titre': "Modifier la vidéo"})

@user_passes_test(is_superuser)
def supprimer_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('galerie:admin_videos')
    return render(request, 'galerie/admin/confirm_delete.html', {'objet': video})