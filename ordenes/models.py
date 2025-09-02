from django.db import models
from django.conf import settings  # para usar AUTH_USER_MODEL

class Orden(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ordenes', null=True, blank=True)
    nombre_cliente = models.CharField(max_length=100)
    correo = models.EmailField()
    direccion = models.TextField()
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE, related_name='ordenes')
    cantidad = models.PositiveIntegerField(default=1)
    creado_en = models.DateTimeField(auto_now_add=True)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"Orden #{self.id} - {self.nombre_cliente}"
