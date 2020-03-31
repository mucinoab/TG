from django.contrib import admin

# Register your models here.

from .models import Play


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
