import email
from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    auto_comprado = forms.CharField(max_length=30)
    vendedor_nombre = forms.CharField(max_length=30)
   