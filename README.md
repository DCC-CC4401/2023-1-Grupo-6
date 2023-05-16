# OpiCard

OpiCard consiste en un sitio web donde distintos usuarios pueden públicar, leer y comentar reseñas. Para esto, los usuarios deben crear una cuenta en el sitio, la cual le será útil para comentar reseñas bajo su propio nickname, crear, modificar y eliminar sus propias reseñas, puntuar otras reseñas, entre otras funcionalidades.\
\
El sitio cuenta con una página de inicio de sesión, una página de registro de nuevos usuarios, una página de inicio con las últimas 5 reseñas publicadas de otros usuarios, y una página donde el usuario puede ver su perfil con sus propias reseñas. Además cuenta con formularios para las distintas funcionalidades, como formulario de inicio de sesión, formulario de registro de usuario, formulario de creación de reseña y formulario de comentarios.\
\
Para registrarse, el usuario debe ingresar su nombre, apellido, país, fecha de nacimiento, un username único, su e-mail de registro y una contraseña que luego debe repetir por seguridad. Una vez registrado, será redireccionado a la página de inicio de sesión, donde puede iniciar sesíon con su username y contraseña. Con esto el usuario ya puede crear reseñas, ver otras reseñas y hacer comentarios. Para crear una nueva reseña debe ingresar el nombre del producto, el contenido de su reseña, la categoría a la que pertenece el producto y una puntuación en estrellas de 1 a 5. Una vez publicada, el autor de esta reseña puede modificarla o eliminarla cuando desee. Para crear un comentario, el usuario debe ingresar el comentario y publicarlo, el cual aparecerá junto a su username. También puede puntuar las reseñas de otros usuarios según si le gustan o no.

## Instalación
Para la instalación de este proyecto es necesario tener instalado git en su computador.\
\
Pasos a seguir:\
1. Clonar el repositorio en el directorio deseado
2. Crear ambiente virtual con el siguiente comando:
```
$ python -m venv env
```
3. Activar el ambiente virtual:
Windows:
```
> auxiliar\Scripts\activate
```
Linux:
```
$ source env\Scripts\activate
```
4. Instalar librerías:
```
$ pip install -r requirements.txt
```
5. Crear directorio migrations y base de datos:
```
$ python manage.py makemigrations todoapp categorias
$ python manage.py migrate
```
6. Ejecutar el servidor:
```
$ python manage.py runserver
```
7. Entrar a 127.0.0.1:8000/register

### Models ###
-User
Almacena info de los usuarios: username, nombre, apellido, contraseña, país, edad, email.

-Review
Almacena info de las reviews: usuario creador, nombre del producto, categoría, contenido, puntuacion del creador,
    likes, dislikes.

-Reviews_Username
Almacena la info que conecta un usuario con sus reseñas: usuario creador, id_reseña

-ReviewLikes:
Almacena la info que conecta un usuario con la reseña en la que votó: id_reseña, username, vote

-Comments:
Almacena la info que conecta un usuario con la reseña en la que comentó: id_review, username, creation_date, content
