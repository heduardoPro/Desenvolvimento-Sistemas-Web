from django.contrib import admin
from discos import models
# Register your models here.

@admin.register(models.Discos)
class DiscosAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'selo_fotografico', 'ano', 'pais', 'genero', 'quantidade',
    ordering = '-id',