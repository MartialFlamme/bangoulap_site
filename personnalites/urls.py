from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "personnalites"

urlpatterns = [
    path('', views.liste_personnalites, name='liste'),
    path('<slug:slug>/', views.detail_personnalite, name='detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)