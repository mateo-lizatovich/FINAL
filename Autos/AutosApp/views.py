from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def index(request):
    autos = Auto.objects.all()
    ctx = {'autos': autos}

    return render(request,"AutosApp/index.html", ctx)
   
   
def autos(request):
    autos = Auto.objects.all()
    return render(request,'AutosApp/autos.html',{'autos': autos})

def vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request,'AutosApp/vendedores.html', {'vendedores': vendedores})

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request,'AutosApp/clientes.html', {'clientes': clientes})

