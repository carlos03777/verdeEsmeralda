

# Register your models here.
from django.contrib import admin
from .models import Taller

@admin.register(Taller)
class TallerAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'hora', 'precio')
