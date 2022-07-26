from enum import auto
from django.urls import path, include
from .views import *
from django.contrib import admin


urlpatterns= [
    path('', inicio, name = "inicio"),
    path('inicio_de_sesion', inicio_de_sesion, name = "inicio_de_sesion"),
    path('register', register_request, name="register"),
    path('logout', logout_request, name="logout"),
    path('editar_perfil', editar_perfil, name = "editar_perfil"),

    
    
    path('vendedores/',vendedores, name = "vendedores"),
    path('clientes/', clientes, name = "clientes"),
    path('autos/', autos, name = "autos"),
    path('base/', base),
    path('buscar_auto/', buscar_auto, name = "buscar_auto"),
    path('crear_cliente/', crear_cliente, name = "crear_cliente"),
    path('eliminar_cliente/<cliente_id>', eliminar_cliente, name = "eliminar_cliente"),
    path('editar_cliente/<cliente_id>', editar_cliente, name = "editar_cliente"),
    
    
    path('clientes/list', ClienteList.as_view(), name="clientes_list"),
    path(r'^(?P<pk>\d+)$', ClienteDetail.as_view(), name="clientes_detail"),
    path(r'^nuevo$', ClienteCreate.as_view(), name="clientes_create"),
    path(r'^editar/(?P<pk>\d+)$', ClienteUpdate.as_view(), name="clientes_update"),
    path(r'^eliminar/(?P<pk>\d+)$', ClienteDelete.as_view(), name="clientes_delete"),
]