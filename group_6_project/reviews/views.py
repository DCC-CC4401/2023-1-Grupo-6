from django.shortcuts import render, redirect
from .forms import LogInForm, RegisterForm, CreateReviewForm
from reviews.models import User, Review
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
import json
# Create your views here.

# Esta función maneja el proceso de log in del usuario.
#     Cuando un usuario envía un formulario de log in, esta función presenta un POST request,
#     valida el formulario, autentica las credenciales, ingresa al usuario 
#     y lo redirige a la URL '/ShowReviews/' si todo se realiza exitosamente.
#     Si no es válido o la autenticación falla, al usuario se le presenta un mensaje de error.
#     Si es u GET request el que se recibe, al usuario se le presenta un formulario de ingreso para llenar.
def Login(request):
    # Si es un método POST, se toma un formulario con los datos ingresados
    if request.method == 'POST':
        form = LogInForm(request.POST)
        # Se verifica que todos los campos sean válidos.
        if form.is_valid():
            # Si son válidos, se recupera el nickname y la contraseña ingresados
            username = form.cleaned_data['nick_name']
            password = form.cleaned_data['password']
            # Se autentica que sean un usuario existente
            user = authenticate(request, username=username, password=password)
            # Si el usuario no es nulo
            if user is not None:
                # Se ingresa con el usuario en '/ShowReviews/'
                login(request, user)
                return redirect('/ShowReviews/')
            # Si el usuario es nulo
            else:
                # Se da un mensaje de error
                form.add_error(None, 'Invalid username or password')
    # Si es un método GET, se entrega un formulario para ser llenado 
    else:
        form = LogInForm()
    return render(request, 'reviews/LogIn.html', {'form': form})



# Esta función maneja el proceso de registro del usuario.
#     Cuando un usuario envía un formulario de registro, esta función presenta un POST request,
#     valida el formulario, recoge los datos ingresados, guarda al usuario
#     y lo redirige a la URL '/login/' si todo se realiza exitosamente.
#     Si es un GET request el que se recibe, al usuario se le presenta un formulario de registro para llenar.
def register_user(request):
    # Si es un método GET, se entrega un formulario para ser llenado
    if request.method == 'GET': 
        form = RegisterForm()
        return render(request, "reviews/register_user.html", {'form': form}) 
    
    # Si es un método POST, se recogen los datos y se agrega un usuario
    elif request.method == 'POST': 
        #Tomar los elementos del formulario que vienen en request.POST
        form = RegisterForm(request.POST)
        # Si los datos son válidos según el formulario 
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name') # El primer nombre
            last_name = form.cleaned_data.get('last_name') # El segundo nombre
            username=form.cleaned_data.get('username') # El nombre de usuario
            password=form.cleaned_data.get('password') # Contraseña
            email=form.cleaned_data.get('email') # Dirección de correo electrónico
            country=form.cleaned_data.get('country') # País
            birthdate=form.cleaned_data.get('birth_date') # Fecha de nacimiento
            # Se crea un usuario con los datos ingresador
            user = User.objects.create_user(first_name=first_name, last_name=last_name,username=username, password=password, email=email, country=country, birthdate=birthdate) 
            # Redirecciona a login
            return HttpResponseRedirect('/login/')
        
    
# Se lee el .json con las categorías de las reseñas. Serán utilizadas para recuperar el nombre de la categoria.
with open('reviews/assets/categories.json', 'r') as f:
            categories = json.load(f)


# Esta función maneja el proceso de creación de reviews.
#     Cuando un usuario envía un formulario de creación de review, esta función presenta un POST request,
#     valida el formulario y que el usuario esté autenticado, recoge los datos ingresados, crea una review
#     y lo redirige a la URL '/ShowReviews/' si todo se realiza exitosamente.
#     Si es un GET request el que se recibe, al usuario se le presenta un formulario de registro para llenar.
def CreateReview(request):
    if request.user.is_authenticated:
         # Si es un método POST, se recogen los datos y se agrega una review al usuario
        if request.method == 'POST':
            form = CreateReviewForm(request.POST)
            # Si los datos son válidos según el formulario y el usuario está ingresado
            if form.is_valid() and request.user.is_authenticated:
                product_name = form.cleaned_data["product_name"] # Nombre del producto
                content = form.cleaned_data["content"] # Contenido de la review
                category = form.cleaned_data["category"] # Categoría
                punctuation = form.cleaned_data["punctuation"] # Puntuación 
                # Se crea la Review
                review = Review(product_name=product_name, category=category, content=content, punctuation=punctuation, author_nickname=request.user)
                # Guarda la Review
                review.save()
                # Redirige a '/ShowReviews/'
                return redirect('/ShowReviews/')
        else:
            # Si es un método GET, se entrega un formulario para ser llenado
            form = CreateReviewForm()
        return render(request, 'reviews/CreateReview.html', {'form': form})
    else:
            return redirect('/login/')
    
# Se dirige al template showReview.html donde se cargan las últimas 5 reviews
def ShowReviews(request):
        # Se recuperan las 5 últimas reseñas
        last_five_objects = Review.objects.order_by('-id')[:5]
        return render(request, 'reviews/showReview.html', {'reviews': last_five_objects, 'categories': categories})

# Se dirige al template showMyReview.html donde se cargan las últimas 5 reviews
def ShowMyReviews(request):
        print(request)
        # Se recuperan las reseñas del usuario
        if request.user.is_authenticated:
            user_objects = Review.objects.filter(author_nickname=request.user)
            return render(request, 'reviews/myReviews.html', {'reviews': user_objects, 'categories': categories})
        else: 
            return redirect('/login/')

# Se lleva a una página de modificación de la Review
def ModifyReview(request, review_id):
    # Recupera la review con id "review_id"
    if request.method == 'GET' and request.user.is_authenticated:
        review = Review.objects.filter(id=review_id)[0]
        # print(review.punctuation)
        PUNCTUATIONS=[
            (1, "ONE_STAR"),
            (2, "TWO_STARS"),
            (3, "THREE_STARS"),
            (4, "FOUR_STARS"),
            (5, "FIVE_STARS"),
        ]
        initial = {"product_name":review.product_name, "category":review.category, "content":review.content, "punctuation":review.punctuation}
        form = CreateReviewForm(initial=initial)
        # Se redirige a '/ShowReviews/'
        return render(request, 'reviews/ModifyReview.html', {'form':form, 'review': review, 'categories': categories})

def ModifiedReview(request, review_id):
    if request.method == 'POST':
        form = CreateReviewForm(request.POST)
        # Si los datos son válidos según el formulario 
        if form.is_valid() and request.user.is_authenticated:
            product_name = form.cleaned_data["product_name"] # Nombre del producto
            content = form.cleaned_data["content"] # Contenido de la review
            category = form.cleaned_data["category"] # Categoría
            punctuation = form.cleaned_data["punctuation"] # Puntuación 
            # Se crea la Review
            review = Review.objects.filter(id=review_id)[0]
            review.product_name=product_name
            review.content=content
            review.category=category
            review.punctuation=punctuation
            # Guarda la Review
            review.save()
            # Redirige a '/myReviews/'
            return redirect('/myReviews/')
     

# Se borra la Review desde ShowReviews
def DeleteReviewSR(request, review_id):    
    # Recupera la review con id "review_id"
    review = Review.objects.filter(id=review_id)
    # Se borra ese objeto
    review.delete()
    # Se redirige a '/ShowReviews/'
    return redirect('/ShowReviews/')

# # Se borra la Review desde myReviews
# def DeleteReviewMR(request, review_id):    
#     # Recupera la review con id "review_id"
#     review = Review.objects.filter(id=review_id)
#     # Se borra ese objeto
#     review.delete()
#     # Se redirige a '/myReviews/'
#     return redirect('/myReviews/')

# Redirige a '/createReview/'
def GoCreateReview(request):
    return redirect('/createReview/')

# Redirige a '/ShowReviews/'
def GoReviews(request):
    return redirect('/ShowReviews/')

# Redirige a '/login/'
def GoLogin(request):
    return redirect('/login/')

# Redirige a '/register_user/'
def GoRegister(request):
    return redirect('/register_user/')

# Renderiza el html de myReviews
def myReviews(request):
    return render(request, 'reviews/myReviews.html')

# Renderiza el html de inicio
def Inicio(request):
    return render(request, 'reviews/Inicio.html')

# Quita la sesión iniciada por el usuario y redirige a '/ShowReviews/'
def LogOut(request):
    logout(request)
    return redirect('/ShowReviews/')