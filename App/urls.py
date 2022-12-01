from django.urls import path
from App.views import *

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('Personas/', formulario_personas, name="Persona"),
    path('compras/', formulario_compras, name="Compras"),
    path('animal/', formulario_animal, name="Animal"),
    path('busquedapersona/', busqueda_persona, name="Busqueda_Persona"),
    path('buscar/', buscar, name="buscar"),
]