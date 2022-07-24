from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def inicio(request):
    
    return render(request,"AutosApp/index.html", {})
   
   
def autos(request):
    autos = Auto.objects.all()
    return render(request,'AutosApp/autos.html',{'autos': autos})

def vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request,'AutosApp/vendedores.html', {'vendedores': vendedores})

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request,'AutosApp/clientes.html', {'clientes': clientes})

def base(request):
    return render(request, 'AutosApp/base.html', {})

def formularios(request):
    return render(request, 'AutosApp/formularios.html', {})

def buscar_auto(request):
    autos = Auto.objects.all()
    return render(request, 'AutosApp/buscar_auto.html', {"autos": autos})

