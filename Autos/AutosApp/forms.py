from dataclasses import fields
import email
from pyexpat import model
from subprocess import CREATE_NO_WINDOW
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    auto_comprado = forms.CharField(max_length=30)
    vendedor_nombre = forms.CharField(max_length=30)

class AutoFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    año = forms.CharField (max_length=30)
    precio = forms.CharField(max_length=30)
  
class UserRegisterForm(UserCreationForm):
    #usuario = forms.CharField(label="Nombre de usuario")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) #para que la contraseña no se vea
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False) # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

        help_texts = {k:"" for k in fields}
        
class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="imagen")    
       
    class Meta():
        model = Avatar
        fields = ['imagen']     
        
