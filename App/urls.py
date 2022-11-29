from django.urls import path
from App.views import inicio

urlpatterns = [
    path('inicio/', inicio),
]