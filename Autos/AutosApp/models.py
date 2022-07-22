
from django.db import models

class Auto(models.Model):
    marca = models.CharField("Marca ",max_length=30)
    modelo = models.CharField("Modelo ", max_length=30)
    año = models.IntegerField("Año: ")
    precio = models.IntegerField("Precio USD$ ")

class Vendedor(models.Model):
    nombre = models.CharField("Nombre ", max_length=30)
    apellido = models.CharField("Apellido ", max_length=30, blank=True, null=True,)
    class Meta:                                     
        verbose_name_plural = "Vendedores"

    

class Cliente(models.Model):
    #from .models import Auto
    nombre= models.CharField("Nombre", max_length=30)
    apellido= models.CharField("Apellido", max_length=30)
    auto_comprado = models.CharField("Auto Comprado", max_length=30,blank=True, null=True)
    vendedor_nombre = models.CharField("Vendedor ", max_length=30, blank=True, null=True)
    





