from django.contrib import admin
from .models import Personnalite

@admin.register(Personnalite)
class PersonnaliteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'fonction', 'slug')
    prepopulated_fields = {'slug': ('nom',)}
    search_fields = ('nom', 'fonction')
