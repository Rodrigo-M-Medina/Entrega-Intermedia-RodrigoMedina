from django.urls import path
from App.views import inicio, formulario_personas

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('formulario/', formulario_personas, name="Formulario"),
]