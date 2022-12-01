from django.shortcuts import render
from App.forms import Form_Persona, Form_Compras
from .models import Persona, Compras
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
    return render(request, "App/Formulario.html", {"form":form})

def formulario_compras(request):
    if request.method=='POST':
        form = Form_Compras(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            persona1= Compras(nombre=informacion['nombre'], edad=informacion['edad'])
            persona1.save()
            return render(request, "App/Inicio.html")
    else:
        form=Form_Compras()
    return render(request, "App/Compras.html", {"form":form})       
   


    