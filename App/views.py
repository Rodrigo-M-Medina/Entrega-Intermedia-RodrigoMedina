from django.shortcuts import render
from App.forms import Form_Persona, Form_Compras, Form_Animal
from .models import Persona, Compras, Animal
from django.http import HttpResponse



def inicio(request):
    return render (request, "App/Inicio.html")

def formulario_personas(request):
    if request.method=='POST':
        form = Form_Persona(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            persona1= Persona(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], edad=informacion['edad'])
            persona1.save()
            return render(request, "App/Inicio.html")
    else:
        form=Form_Persona()
    return render(request, "App/Persona.html", {"form":form})

def formulario_compras(request):
    if request.method=='POST':
        form = Form_Compras(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            persona1= Compras(producto=informacion['producto'], valor=informacion['valor'])
            persona1.save()
            return render(request, "App/Inicio.html")
    else:
        form=Form_Compras()
    return render(request, "App/Compras.html", {"form":form})   


def formulario_animal(request):
    if request.method=='POST':
        form = Form_Animal(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            persona1= Animal(nombre=informacion['nombre'], raza=informacion['raza'], edad=informacion['edad'])
            persona1.save()
            return render(request, "App/Inicio.html")
    else:
        form=Form_Animal()
    return render(request, "App/Animal.html", {"form":form})

def busqueda_persona(request):
    return render (request, "App/Busqueda_Persona.html")

def buscar(request):
    
    if request.GET["nombre"]:

        persona=request.GET["nombre"]

        personas=Persona.objects.filter(nombre=persona)

        return render(request, "App/Buscar_Resultado.html", {"personas":personas})

    else:
        return render (request, "App/Busqueda_Persona.html", {"mensaje":"Esa Persona no existe en la base de datos"})
