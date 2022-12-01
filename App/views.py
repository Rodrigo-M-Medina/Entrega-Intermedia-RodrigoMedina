from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, context, loader
from App.forms import Form_Persona
from .models import Persona


def inicio(request):
    return render (request, "App/Inicio.html")

def formulario_personas(request):
    if request.method=="POST":
        form=formulario_personas(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            edad=informacion["edad"]
            email=informacion["email"]
            persona=Persona(nombre=nombre, apellido=apellido, edad=edad, email=email)
            persona.save()
            return render (request, "App/Formulario.html", {"mensaje": "Persona Registrada correctamente"})
    else:
        formulario=Form_Persona()

    return render(request, "App/Formulario.html", {"form":formulario})
