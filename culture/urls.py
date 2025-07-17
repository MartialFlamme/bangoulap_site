from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'culture'

urlpatterns = [
    path('', RedirectView.as_view(url='danses/')),  # ← redirection
    path('danses/', views.danses, name='danses'),
    path('festivals/', views.festivals, name='festivals'),
    path('structure/', views.structure, name='structure'),
]
