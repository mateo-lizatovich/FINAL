from enum import auto
from django.urls import path, include
from .views import *
from django.contrib import admin


urlpatterns= [
    path('vendedores/', vendedores),
    path('clientes/', clientes),
    path('autos/', autos),
    
]