from django.shortcuts import render, redirect
from .forms import LogInForm, RegisterForm, CreateReviewForm
from reviews.models import User, Review
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
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

def register_user(request):
    if request.method == 'GET': #Si estamos cargando la página}
        form = RegisterForm()
        return render(request, "reviews/register_user.html", {'form': form}) #Mostrar el template

    elif request.method == 'POST': #Si estamos recibiendo el form de registro
     #Tomar los elementos del formulario que vienen en request.POST
        # TODO: authenticate user and redirect to home page
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name') 
            last_name = form.cleaned_data.get('last_name') 
            username=form.cleaned_data.get('username') 
            password=form.cleaned_data.get('password') 
            email=form.cleaned_data.get('email')
            country=form.cleaned_data.get('country')
            birthdate=form.cleaned_data.get('birth_date')
            user = User.objects.create_user(first_name=first_name, last_name=last_name,username=username, password=password, email=email, country=country, birthdate=birthdate) 
            return HttpResponseRedirect('/login/')
        
     #Crear el nuevo usuario
    
     #Redireccionar la página /tareas
     #return HttpResponseRedirect('/tareas')

def CreateReview(request):
    if request.method == 'POST':
        form = CreateReviewForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data["product_name"]
            content = form.cleaned_data["content"]
            category = form.cleaned_data["category"]
            punctuation = form.cleaned_data["punctutation"]
            review = Review(product_name=product_name, category=category, content=content, punctuation=punctuation)
            review.save()
            last_five_objects = Review.objects.order_by('-id')[:5]
            return render(request, 'reviews/showReview.html', {'reviews': last_five_objects})
            
    else:
        form = CreateReviewForm()
    return render(request, 'reviews/CreateReview.html', {'form': form})


def ShowReviews(request):
        last_five_objects = Review.objects.order_by('-id')[:5]
        return render(request, 'reviews/showReview.html', {'reviews': last_five_objects})


def DeleteReview(request, review_id):
    review = Review.objects.filter(id=review_id)
    review.delete()
    return redirect('/ShowReviews/')

def GoCreateReview(request):
    return redirect('/createReview/')

def GoReviews(request):
    return redirect('/ShowReviews/')

def GoLogin(request):
    return redirect('/login/')

def GoRegister(request):
    return redirect('/register_user/')

def Inicio(request):
    return render(request, 'reviews/Inicio.html')

def LogOut(request):
    logout(request)
    return redirect('/ShowReviews/')