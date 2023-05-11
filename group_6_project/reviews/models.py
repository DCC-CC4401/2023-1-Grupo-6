from django.utils import timezone
from django.db import models


# Create your models here.

# Se trae la clase AbstractUser del módulo "models" del paquete "auth"
from django.contrib.auth.models import AbstractUser


# Modelo personalizado de usuario llamado User que hereda de AbstractUser. El modelo User incluye 
# tres campos adicionales: birthdate, password y country.
class User(AbstractUser):
   # Tipo fecha. Con null=True y blank=True puede tener su espacio vacío o un nulo en la bdd.
   birthdate = models.DateField(null=True, blank=True)
   # Campo de carácteres. Máximo de 50 carácteres.
   password = models.CharField(max_length=50)
   # Campo de carácteres. Tiene largo máximo de 50 carácteres, puede estar vacío o ser NULL en la bdd.
   country = models.CharField(max_length=50,  blank=True, null=True)

# devuelve la edad del usuario en años, calculada a partir de su fecha de nacimiento (birthdate). 
# Este método utiliza la biblioteca de timezone de Django para obtener la fecha actual y calcular 
# la edad del usuario en base a la fecha actual y la fecha de nacimiento. Si birthdate no está 
# definido para el usuario, el método devuelve None
   def get_age(self):
         if self.birthdate:
            today = timezone.now().date()
            return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
         else:
            return None
    


# Modelo llamado Review que hereda de la clase models.Model de Django. El modelo 
# Review representa una reseña de un producto que incluye información como el nombre del producto, el 
# contenido de la reseña y la puntuación.
class Review(models.Model):  # Todolist able name that inherits models.Model
    # Campo de caracteres (máximo 100) que almacena el nombre del producto.
    product_name = models.CharField(max_length=100)# autodesc
    # Campo de caracteres, esperamos que contenga las categorías a las que puede pertenecer el producto 
    category = models.CharField(max_length=50,  blank=True, null=True)
    # Campo de texto  que almacena el contenido de la reseña, con una longitud máxima de 500 caracteres.
    content =	models.TextField(max_length=500)# donde se obtuvo, es un alimento, herramienta, etc. como se utiliza, precio
    # Campo de fecha. Contiene la fecha en que se creó la reseña
    creation_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))# autodesc

   # Puntuaciones que puede tener una reseña
    CATEGORIES = [
       (1, "ONE_STAR"),
       (2, "TWO_STARS"),
       (3, "THREE_STARS"),
       (4, "FOUR_STARS"),
       (5, "FIVE_STARS"),
    ]
   # Campo de enteros. Puntuación dada por el creador de la reseña
    punctuation = models.IntegerField(choices=CATEGORIES, default=CATEGORIES[2][1], help_text="Puntuación")
   # Campo de enteros. Contiene la cantidad de "me gusta" que ha recibido de otros usuarios
   #  likes = models.IntegerField(null=True, default=0)
      # Campo de enteros. Contiene la cantidad de "me gusta" que ha recibido de otros usuarios
   #  dislikes = models.IntegerField(null=True, default=0)

   #  author_nickname =  models.ForeignKey(User, default="general", on_delete=models.CASCADE)# autodesc

# Modelo que hereda de la clase Model del módulo models de Django. Tiene los campos "id_reseña" y "username", 
# para tener almacenado a qué username corresponde qué reseña
class Reviews_Username(models.Model):
   id_review = models.ForeignKey(Review, default="general", on_delete=models.CASCADE)
   username = models.ForeignKey(User, default="general", on_delete=models.CASCADE)

# Modelo que hereda de la clase Model del módulo models de Django. Tiene los campos "id_reseña" y "username", 
# para tener almacenado si un username ha votado "like" o "dislike" en una reseña.
class ReviewLikes(models.Model):
    id_review = models.ForeignKey(Review, default="general", on_delete=models.CASCADE)
    username = models.ForeignKey(User, default="general", on_delete=models.CASCADE)
    vote = models.IntegerField(default=0)

# Modelo que hereda de la clase Model del módulo models de Django. Tiene los campos "id_reseña", "comentador"
# , fecha_creacion y contenido, para tener almacenado a qué username corresponde qué comentario, en qué reseña
# en qué momento y cual es el contenido.
class Comments(models.Model):
    id_review = models.ForeignKey(Review, default="general", on_delete=models.CASCADE)
    username = models.ForeignKey(User, default="general", on_delete=models.CASCADE)
    creation_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))# autodesc
    content =	models.TextField(max_length=500, null=False, blank=False, default="No comment")


   