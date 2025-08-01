from django.urls import path
from . import views

app_name = 'admin_custom'

urlpatterns = [
    path('login/', views.custom_login, name='login'),  # vue personnalisée
    path('logout/', views.custom_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # gestion des utilisateurs
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:user_id>/edit/', views.user_edit, name='user_edit'),
    path('users/<int:user_id>/delete/', views.user_delete, name='user_delete'),
]
