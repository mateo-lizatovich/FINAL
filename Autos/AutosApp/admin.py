from django.contrib import admin

from AutosApp.models import *


class AutoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo','año','precio')
    search_fields = ('marca', 'modelo','año','precio')


class VendedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido')
    search_fields = ('nombre', 'apellido')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','auto_comprado','vendedor_nombre')
    search_fields = ('nombre', 'apellido','auto_comprado','vendedor_nombre')





admin.site.register(Auto, AutoAdmin)
admin.site.register(Vendedor, VendedorAdmin)      
admin.site.register(Cliente, ClienteAdmin)