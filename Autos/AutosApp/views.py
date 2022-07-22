from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def index(request):
    autos = Auto.objects.all()
    ctx = {'autos': autos}

    return render(request,"AutosApp/index.html", ctx)
