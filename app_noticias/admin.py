from django.contrib import admin
from .models import Noticia
# Register your models here.

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')
    search_fields = ('titulo', 'descripcion')