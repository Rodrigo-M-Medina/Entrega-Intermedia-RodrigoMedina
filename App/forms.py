from django import forms

class Form_Persona(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    email=forms.EmailField()

class Form_Compras(forms.Form):
    producto=forms.CharField(max_length=50)
    valor=forms.FloatField()

class Form_Animal(forms.Form):
    nombre=forms.CharField(max_length=50)
    raza=forms.CharField(max_length=50)
    edad=forms.IntegerField()




