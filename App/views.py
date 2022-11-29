from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, context, loader

def inicio(request):
    return render (request, "App/Inicio.html")
