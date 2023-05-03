from django.utils import timezone
from django.db import models
# import json

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   birthdate = models.DateField(null=True, blank=True)
   password = models.CharField(max_length=50)
   country = models.CharField(max_length=50,  blank=True, null=True)


   def get_age(self):
         if self.birthdate:
            today = timezone.now().date()
            return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
         else:
            return None
    

class Review(models.Model):  # Todolist able name that inherits models.Model
    # categoria = models.ForeignKey(categories, default="general", on_delete=models.CASCADE)  
    nombre_producto = models.CharField(max_length=100)# autodesc
    contenido =	models.TextField(max_length=500)# donde se obtuvo, es un alimento, herramienta, etc. como se utiliza, precio
    fecha_creacion = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))# autodesc
    CHOICES = [
       ("ONE_STAR", 1),
       ("TWO_STARS", 2),
       ("THREE_STARS", 3),
       ("FOUR_STARS", 4),
       ("FIVE_STARS", 5),
    ]
    puntuacion = models.IntegerField(choices=CHOICES)# el conjunto de todas las ponderaciones dada la cantidad de valoraciones y el clasificador elegido
    likes = models.IntegerField(null=True, default=0)
    dislikes = models.IntegerField(null=True, default=0)
    cantidad_votantes =	models.IntegerField(null=True, default=0)# contador de la cantidad de reseñas
    nick_autor =  models.ForeignKey(User, default="general", on_delete=models.CASCADE)# autodesc


class Reviews_Username(models.Model):
   id_reseña = models.ForeignKey(Review, default="general", on_delete=models.CASCADE)
   username = models.ForeignKey(User, default="general", on_delete=models.CASCADE)

class Comments(models.Model):
    id_reseña = models.ForeignKey(Review, default="general", on_delete=models.CASCADE)
    comentador = models.ForeignKey(User, default="general", on_delete=models.CASCADE)
    fecha_creacion = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))# autodesc


   