# carrito/views.py

from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from productos.models import Producto
from .cart import Cart


def ver_carrito(request):
    """
    Muestra el carrito con los productos que tiene el usuario en sesión.
    """
    cart = Cart(request)
    return render(request, "carrito/ver_carrito.html", {"cart": cart})


def agregar_al_carrito(request, producto_id):
    """
    Agrega un producto al carrito según su ID.
    """
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=producto_id)
    cart.add(producto)
    return redirect(request.META.get("HTTP_REFERER", "productos-index"))     # Redirige a la página anterior, no al carrito

# carrito/views.py
def actualizar_cantidad(request, producto_id):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == "POST":
        cantidad = int(request.POST.get("cantidad", 1))
        cart.update(producto, cantidad)

    return redirect("carrito-ver")




def eliminar_del_carrito(request, producto_id):
    """
    Elimina un producto del carrito.
    """
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=producto_id)
    cart.remove(producto)
    return redirect("carrito-ver")


def limpiar_carrito(request):
    """
    Limpia todo el carrito.
    """
    cart = Cart(request)
    cart.clear()
    return redirect("carrito-ver")


def checkout(request):
    return HttpResponse("Aquí irá el proceso de checkout / pago.")