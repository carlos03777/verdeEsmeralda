

# Register your models here.
from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    search_fields = ('nombre',)          # barra de búsqueda por nombre
    list_filter = ('precio',) 