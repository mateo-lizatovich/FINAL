import re
from django import http
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from jmespath import search
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.db.models import Q
from .forms import ClienteFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required





def inicio(request):
    
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(usuario = request.user)
        except:
            avatar = None    
        return render(request,"AutosApp/index.html", {"avatar": avatar})
    
    return render(request,"AutosApp/index.html", {})

def inicio_de_sesion(request):
    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("inicio_de_sesion")
        else:
            return redirect("inicio_de_sesion")
    
    form = AuthenticationForm()
    
    return render(request, 'AutosApp/login.html',{"form":form})
  
def register_request(request):
    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
        #form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') # es la primer contraseña, no la confirmacion

            form.save() # registramos el usuario
            # iniciamos la sesion
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
            
        return render(request, 'AutosApp/register.html', {"form":form}) 
    
    form = UserCreationForm()
    #form = UserRegisterForm()
    
    return render(request, 'AutosApp/register.html', {"form":form}) 

def logout_request(request):
    logout(request)
    return redirect("inicio")
 
@login_required     
def editar_perfil(request):
    user = request.user
    
    if request.method == "POST":
        
        form = UserEditForm(request.POST) # cargamos datos llenados
        
        if form.is_valid():

            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            # user.password = info["password1"]

            user.save()

            return redirect("inicio")
        
    else:
        form = UserEditForm(initial = {"email": user.email} )
    
    return render(request, 'AutosApp/editar_perfil.html', {"form": form})
   
@staff_member_required
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


    