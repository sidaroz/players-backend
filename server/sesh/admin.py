from django.contrib import admin
from . import models

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'area', 'difficulty', 'time', 'players_needed', 'description', 'player')

# admin.site.register(models.Area)


