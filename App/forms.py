from django import forms

class Form_Persona(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    email=forms.EmailField()

class Form_Compras(forms.Form):
    nombre=forms.CharField(max_length=50)
    edad=forms.IntegerField()



