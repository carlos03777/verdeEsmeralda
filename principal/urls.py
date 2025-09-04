#principal/urls.py

from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='home'),  # o cualquier vista inicial
    path('', views.home, name='home'),

]

