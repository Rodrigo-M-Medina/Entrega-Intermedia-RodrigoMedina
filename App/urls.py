from django.urls import path
from App.views import inicio, formulario

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('formulario/', formulario, name="formulario"),
]