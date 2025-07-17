# dons/admin.py
from django.contrib import admin
from .models import Don

@admin.register(Don)
class DonAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'montant', 'moyen', 'projet', 'created_at')
    search_fields = ('nom', 'email')
    list_filter = ('moyen', 'created_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
