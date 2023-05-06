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
    product_name = models.CharField(max_length=100)# autodesc
    content =	models.TextField(max_length=500)# donde se obtuvo, es un alimento, herramienta, etc. como se utiliza, precio
   #  creation_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))# autodesc
    CATEGORIES = [
       (1, "ONE_STAR"),
       (2, "TWO_STARS"),
       (3, "THREE_STARS"),
       (4, "FOUR_STARS"),
       (5, "FIVE_STARS"),
    ]
    punctuation = models.IntegerField(choices=CATEGORIES, default=CATEGORIES[2][1], help_text="Puntuación")# el conjunto de todas las ponderaciones dada la cantidad de valoraciones y el clasificador elegido
   #  likes = models.IntegerField(null=True, default=0)
   #  dislikes = models.IntegerField(null=True, default=0)
   #  votes =	models.IntegerField(null=True, default=0)# contador de la cantidad de reseñas
   #  author_nickname =  models.ForeignKey(User, default="general", on_delete=models.CASCADE)# autodesc


class Reviews_Username(models.Model):
   id_reseña = models.ForeignKey(Review, default="general", on_delete=models.CASCADE)
   username = models.ForeignKey(User, default="general", on_delete=models.CASCADE)

class Comments(models.Model):
    id_reseña = models.ForeignKey(Review, default="general", on_delete=models.CASCADE)
    comentador = models.ForeignKey(User, default="general", on_delete=models.CASCADE)
    fecha_creacion = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))# autodesc


   