from django.shortcuts import render
from .forms import LogInForm, RegisterForm
from reviews.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from .forms import LogInForm, CreateReviewForm
# Create your views here.

def Login(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            # TODO: authenticate user and redirect to home page
            pass
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
            # TODO: authenticate user and redirect to home page
            pass
    else:
        form = CreateReviewForm()
    return render(request, 'reviews/CreateReview.html', {'form': form})

