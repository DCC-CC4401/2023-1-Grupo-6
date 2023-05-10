# 2023-1-Grupo-6







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