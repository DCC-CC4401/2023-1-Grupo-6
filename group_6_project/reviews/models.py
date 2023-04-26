from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  paises = [('La','La'),('El','El'), ('Le','Le'),('Otro','Otro')]
  pais = models.CharField(max_length=5,choices=paises)
  apodo = models.CharField(max_length=30)
    