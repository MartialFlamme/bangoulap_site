from django import forms
from .models import Photo, Video

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['titre', 'image', 'evenement']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['titre', 'youtube_id']
