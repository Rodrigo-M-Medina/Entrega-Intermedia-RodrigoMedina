from django.db import models

class Persona(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    email=models.EmailField()
    """def __str__(self):
        return self.nombre+" "+self.apellido+" "+str(self.edad)+" "+self.email"""

class usuario(models.Model):
    pass
