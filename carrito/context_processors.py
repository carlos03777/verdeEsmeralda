from .cart import Cart

def carrito_context(request):
    cart = Cart(request)
    return {
        "carrito_cantidad": len(cart),  # cantidad total de ítems
        "carrito": cart  # por si lo quieres usar en otras plantillas
    }
