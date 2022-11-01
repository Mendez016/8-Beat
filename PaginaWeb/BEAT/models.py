from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.
class usuario(models.Model):
    nombre=models.CharField(max_length=50)
    password=models.CharField(max_length=30)
    registro=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre

class cancion(models.Model):
    name=models.CharField(max_length=50)
    imagenSec=models.CharField(max_length=100)
    audioSec=models.CharField(max_length=100)
    Prim=models.CharField(max_length=100)

class state(models.Model):
    status=models.CharField(max_length=2)