from enum import auto
from django.urls import path, include
from .views import *
from django.contrib import admin


urlpatterns= [
    path('', inicio, name = "inicio"),
    path('vendedores/',vendedores, name = "vendedores"),
    path('clientes/', clientes, name = "clientes"),
    path('autos/', autos, name = "autos"),
    path('base/', base),
    path('buscar_auto/', buscar_auto, name = "buscar_auto"),
    path('crear_cliente/', crear_cliente, name = "crear_cliente"),
    path('eliminar_cliente/<cliente_id>', eliminar_cliente, name = "eliminar_cliente"),
    path('editar_cliente/<cliente_id>', editar_cliente, name = "editar_cliente"),
]