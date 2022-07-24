from django.shortcuts import render, redirect
from django.http import HttpResponse
#from jmespath import search
from .models import *
from django.db.models import Q

def inicio(request):
    
    return render(request,"AutosApp/index.html", {})


   
   
def autos(request):
    if request.method == "POST":
        
        search = request.POST ["search"]
        
        if search != "":
            autos = Auto.objects.filter( Q(marca__icontains=search) | Q(modelo__icontains=search) | Q(año__icontains=search)| Q(precio__icontains=search)).values()
            return render(request,'AutosApp/autos.html',{'autos': autos, "search":True, "busqueda":search})
        
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
    if request.method == "POST":
        
        marca = request.POST["marca"]
        
        marcas = Auto.objects.filter(marca__icontains = marca)
        
        return render(request, 'AutosApp/buscar_auto.html', {"marcas": marcas})

    else:
        marcas = []
        return render(request, 'AutosApp/buscar_auto.html', {"marcas": marcas})
    

