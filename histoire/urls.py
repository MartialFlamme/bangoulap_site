from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'histoire'

urlpatterns = [
    path('', RedirectView.as_view(url='origines/')),  # ✅ redirige vers la 1re page
    path('origines/', views.origines, name='origines'),
    path('sites-touristiques/', views.sites_touristiques, name='sites_touristiques'),
]
