from django.contrib import admin
from .models import Actualite

@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date', 'publie')
    prepopulated_fields = {'slug': ('titre',)}  # Auto-remplit le slug depuis le titre
    list_filter = ('publie', 'date')
