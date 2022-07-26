from django.db import models
from django.contrib.auth.models import User


class Avatar(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatar/', blank=True, null=True)

class Auto(models.Model):
    marca = models.CharField("Marca ",max_length=30)
    modelo = models.CharField("Modelo ", max_length=30)
    año = models.IntegerField("Año: ")
    precio = models.IntegerField("Precio USD$ ")
    def __str__(self):
         return f"Marca: {self.marca} - Modelo: {self.modelo} - Año: {self.año} - Precio: {self.precio} "

class Vendedor(models.Model):
    nombre = models.CharField("Nombre ", max_length=30)
    apellido = models.CharField("Apellido ", max_length=30, blank=True, null=True,)
    class Meta:                                     
        verbose_name_plural = "Vendedores"
    def __str__(self):
         return f"Nombre: {self.nombre} - Apellido: {self.apellido}"

class Cliente(models.Model):
    #from .models import Auto
    nombre= models.CharField("Nombre", max_length=30)
    apellido= models.CharField("Apellido", max_length=30)
    auto_comprado = models.CharField("Auto Comprado", max_length=30,blank=True, null=True)
    vendedor_nombre = models.CharField("Vendedor ", max_length=30, blank=True, null=True)
    def __str__(self):
         return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Vehiculo comprado: {self.auto_comprado} - Vendedor: {self.vendedor_nombre} "
         
    





