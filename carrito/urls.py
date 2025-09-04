# carrito/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_carrito, name='carrito-ver'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='carrito-agregar'),
    path('actualizar/<int:producto_id>/', views.actualizar_cantidad, name='carrito-actualizar'),
    path('eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='carrito-eliminar'),
    path('limpiar/', views.limpiar_carrito, name='carrito-limpiar'),
    path('checkout/', views.checkout, name='checkout'),
]
