# carrito/cart.py
from productos.models import Producto

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, producto, cantidad=1, update=False):
        """
        Agrega un producto al carrito o actualiza la cantidad.
        """
        producto_id = str(producto.id)
        if producto_id not in self.cart:
            self.cart[producto_id] = {
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 0,
            }
        if update:
            self.cart[producto_id]["cantidad"] = cantidad
        else:
            self.cart[producto_id]["cantidad"] += cantidad
        self.save()

    def update(self, producto, cantidad):
        """
        Actualiza la cantidad de un producto.
        """
        producto_id = str(producto.id)
        if producto_id in self.cart:
            self.cart[producto_id]["cantidad"] = cantidad
            self.save()

    def remove(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()

    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True

    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def __iter__(self):
        """
        Itera sobre los items del carrito y calcula subtotal.
        """
        productos = Producto.objects.filter(id__in=self.cart.keys())
        for producto in productos:
            item = self.cart[str(producto.id)]
            item["producto"] = producto
            item["subtotal"] = float(item["precio"]) * item["cantidad"]
            yield item

    def __len__(self):
        """
        Número total de productos en el carrito.
        """
        return sum(item["cantidad"] for item in self.cart.values())

    def get_total(self):
        """
        Total general del carrito.
        """
        return sum(float(item["precio"]) * item["cantidad"] for item in self.cart.values())
