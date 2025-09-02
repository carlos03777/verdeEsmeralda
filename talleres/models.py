from django.db import models

# Create your models here.

class Taller(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='talleres/', blank=True, null=True)

    def __str__(self):
        return self.titulo
