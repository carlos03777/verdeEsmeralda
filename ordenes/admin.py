

# Register your models here.
from django.contrib import admin
from .models import Orden

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_cliente', 'producto', 'cantidad', 'pagado', 'creado_en')
    list_filter = ('pagado', 'creado_en')
    search_fields = ('nombre_cliente', 'correo', 'producto__nombre')
