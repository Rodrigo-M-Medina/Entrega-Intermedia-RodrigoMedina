from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, context, loader
from App.forms import Form_Persona


def inicio(request):
    return render (request, "App/Inicio.html")

def formulario(request):
    return render (request, "App/Formulario.html")
