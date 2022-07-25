import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from jmespath import search
from .models import *
from django.db.models import Q
from .forms import ClienteFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    
def crear_cliente(request):
    if request.method == "POST":
        
        formulario = ClienteFormulario(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            cliente = Cliente(nombre = info["nombre"], apellido = info["apellido"], auto_comprado = info["auto_comprado"], vendedor_nombre = info["vendedor_nombre"])
            cliente.save()
            
            return redirect("clientes")
            
        return render(request, 'AutosApp/formularios_clientes.html', {"form": formulario})

    formulario = ClienteFormulario()
    return render(request, 'AutosApp/formularios_clientes.html', {"form": formulario})

def eliminar_cliente(request,cliente_id):
    
     cliente = Cliente.objects.get(id=cliente_id)
     cliente.delete()
     
     return redirect("clientes")
 
def editar_cliente(request,cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)

    if request.method == "POST":

        formulario = ClienteFormulario(request.POST)

        if formulario.is_valid():
            
            info_cliente = formulario.cleaned_data
            
            cliente.nombre = info_cliente["nombre"]
            cliente.apellido = info_cliente["apellido"]
            cliente.auto_comprado = info_cliente["auto_comprado"]
            cliente.vendedor_nombre = info_cliente["vendedor_nombre"]
            cliente.save()

            return redirect("clientes")

    # get
    formulario = ClienteFormulario(initial={"nombre":cliente.nombre, "apellido":cliente.apellido, "auto_comprado": cliente.auto_comprado, "vendedor_nombre": cliente.vendedor_nombre})
    
    return render(request,"AutosApp/formularios_clientes.html",{"form":formulario})

class ClienteList(ListView):
    model = Cliente
    template_name = "AutosApp/clientes_list.html"
    
class ClienteDetail(DetailView):
    model = Cliente
    template_name = "AutosApp/clientes_detail.html"
    
class ClienteCreate(CreateView):
    model = Cliente
    success_url = "/autosapp/clientes/list" #segun lucas la primer / es la diferencia entre que ande todo o explote todo
    fields = ["nombre", "apellido", "auto_comprado", "vendedor_nombre"]
    
class ClienteUpdate(UpdateView):
    model = Cliente
    success_url = "/autosapp/clientes/list" #segun lucas la primer / es la diferencia entre que ande todo o explote todo
    fields = ["nombre", "apellido", "auto_comprado", "vendedor_nombre"]
    
class ClienteDelete(DeleteView):
    model = Cliente
    success_url = "/autosapp/clientes/list" 
    