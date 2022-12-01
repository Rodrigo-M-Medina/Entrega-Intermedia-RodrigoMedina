from django.urls import path
from App.views import inicio, formulario_personas, formulario_compras

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('formulario/', formulario_personas, name="Formulario"),
    path('compras/', formulario_compras, name="Compras"),
]