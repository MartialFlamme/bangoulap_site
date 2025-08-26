from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),                     # accueil
    path('culture/', include('culture.urls')),
    path('histoire/', include('histoire.urls')),
    path('actualites/', include('actualites.urls', namespace='actualites')),
    path('personnalites/', include('personnalites.urls')),
    path('associations/', include('associations.urls')),
    path('CODEBA/', include(('CODEBA.urls', 'CODEBA'), namespace='CODEBA')),
    path('galerie/', include('galerie.urls')),
    path("contact/", include("contact.urls", namespace="contact")),
    path('dons/', include('dons.urls', namespace='dons')),
    path('projets/', include('projets.urls', namespace='projets')),
    path("admin-custom/", include("admin_custom.urls", namespace="admin_custom")),
    path("login/", lambda request: redirect("admin_custom:login")),
    path("logout/", lambda request: redirect("admin_custom:logout")),
]
# ✅ Ajoute ceci EN DEHORS de urlpatterns
handler403 = "admin_custom.views.custom_permission_denied_view"

# Servir les fichiers médias et statiques seulement si DEBUG=True ou pour petite prod
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

