from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),                     # accueil
    path('culture/', include('culture.urls')),
    path('histoire/', include('histoire.urls')),
    path('actualites/', include('actualites.urls', namespace='actualites')),
    path('personnalites/', include('personnalites.urls')),
    path('associations/', include('associations.urls')),
    path('education/', include('education.urls')),
    path('galerie/', include('galerie.urls')),
    path("contact/", include("contact.urls", namespace="contact")),
    path('dons/', include('dons.urls', namespace='dons')),
    path('projets/', include('projets.urls', namespace='projets')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)