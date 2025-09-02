from django.shortcuts import render

# Create your views here.
# principal/views.py

'''from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenido a Verde Esmeralda")'''

# views.py en tu app principal
from django.shortcuts import render

def home(request):
    return render(request, 'principal/home.html')

