from enum import auto
from django.urls import path, include
from .views import *
from django.contrib import admin


urlpatterns= [
    path('', inicio, name = "inicio"),
    path('vendedores/', vendedores, name = "vendedores"),
    path('clientes/', clientes, name = "clientes"),
    path('autos/', autos, name = "autos"),
]