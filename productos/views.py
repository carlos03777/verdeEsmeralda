from django.shortcuts import render, get_object_or_404
from .models import Producto

def index(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})
