from django.urls import path
from App.views import inicio, formulario_personas, formulario_compras, formulario_animal, busqueda, buscar

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('Personas/', formulario_personas, name="Persona"),
    path('compras/', formulario_compras, name="Compras"),
    path('animal/', formulario_animal, name="Animal"),
    path('Buscar/', busqueda, name="busqueda"),
    path('buscar/', buscar, name="buscar"),

]