from django import forms
import re
from datetime import date, timedelta
from reviews.models import User, Review, Comments
import json


class LogInForm(forms.Form):
    nick_name = forms.CharField(label="Nickname", widget=forms.TextInput(attrs={'placeholder':'Nombre de usuario', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Contraseña', 'class': 'form-control'}))


with open('reviews/assets/countries.json', 'r') as f:
            countries = json.load(f)

class RegisterForm(forms.Form):
    first_name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'placeholder':'Nombre','class': 'form-control'}))
    last_name = forms.CharField(label="Apellido", required=True,widget=forms.TextInput(attrs={'placeholder':'Apellido','class': 'form-control'}))
    country = forms.ChoiceField(label='Select a country', widget=forms.Select(attrs={'class': 'form-select text-muted'}), choices=[(country['code'], country['name']) for country in countries],  required=True)
    birth_date = forms.DateTimeField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    username = forms.CharField(label="Nombre de usuario", required=True,widget=forms.TextInput(attrs={'placeholder':'Nombre de usuario', 'class': 'form-control'}))
    email = forms.EmailField( required=True, widget=forms.EmailInput(attrs={'placeholder':'Correo electrónico', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Contraseña', 'class': 'form-control'}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Repetir contraseña', 'class': 'form-control'}))

    # Validador de first_name: se verifica que el primer nombre no sea un campo vacío
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'] 
        if not first_name:
            raise forms.ValidationError('No se ingresó nombre.') 
        return first_name
    
    # Validador de last_name: se verifica que el apellido no sea un campo vacío
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'] 
        if not last_name:
            raise forms.ValidationError('No se ingresó apellido.') 
        return last_name
    
    # Validador de birth_date: se verifica que la fecha de nacimiento corresponda con una de hace más de 18 años.
    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date'] 
        fecha_actual = date.today()
        fecha_limite = fecha_actual - timedelta(days=365 * 18)
        print(type(birth_date.date()))
        print(type(fecha_limite))
        age_min = birth_date.date() <= fecha_limite
        if not age_min:
            raise forms.ValidationError('Se debe tener más de 18 años.')      
        return birth_date
    
    # Validador de username: se verifica que el username no sea repetido
    def clean_username(self):
        username = self.cleaned_data['username']
        users = User.objects.filter(username=username).exists()
        if not username:
            raise forms.ValidationError('No se ingresó usuario.') 
        if users:
            print(username)
            raise forms.ValidationError('Ese username ya existe.') 
        return username
    
    # Validador de password: se verifica que la contraseña tenga el largo necesario y tipos de caracteres variados (especiales o dígitos, mayúsculas y minúsculas)
    def clean_password(self):
        password = self.cleaned_data['password']   
        min_length = len(password) >= 8
        uppercase_regex = r'[A-Z]'
        lowercase_regex = r'[a-z]'
        number_special_regex = r'[\d\W]'
        upper = re.search(uppercase_regex, password)
        lower = re.search(lowercase_regex, password)
        number_special = re.search(number_special_regex, password)
        if not min_length:
            raise forms.ValidationError('La contraseña debe tener como mínimo 8 caracteres')  
        if not (upper and lower and number_special):
              raise forms.ValidationError("La contraseña debe tener mayúsculas, minúsculas, y carácteres especiales o dígitos.")   
        return password 
    # Validador de repeat_password: se verifica que la repetición de contraseña tenga el largo necesario y tipos de caracteres variados (especiales o dígitos, mayúsculas y minúsculas)
    def clean_repeat_password(self):
        repeat_password = self.cleaned_data['repeat_password']   
        min_length = len(repeat_password) >= 8
        uppercase_regex = r'[A-Z]'
        lowercase_regex = r'[a-z]'
        number_special_regex = r'[\d\W]'
        upper = re.search(uppercase_regex, repeat_password)
        lower = re.search(lowercase_regex, repeat_password)
        number_special = re.search(number_special_regex, repeat_password)
        if not min_length:
            raise forms.ValidationError('La contraseña debe tener como mínimo 8 caracteres')  
        if not (upper and lower and number_special):
              raise forms.ValidationError("La contraseña debe tener mayúsculas, minúsculas, y carácteres especiales o dígitos.")   
        return repeat_password

    # Validador de email: se verifica que el email tenga estructura de email (algo@fuente.dominio)
    def clean_email(self):
        email = self.cleaned_data['email']  
        regex = r'^[\w\.-]+@\w+\.\w+$'
        correct_email = re.match(regex, email) is not None
        if not correct_email:
            raise forms.ValidationError('El correo ingresado no tiene la estructura correcta.')
        return email      

    # Se verifica que la contraseña y la repetición de contraseña sean iguales
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')
        if password and repeat_password and password != repeat_password:
            self.add_error('password', 'Contraseña y Repetir contraseña no son iguales.')

            
            

with open('reviews/assets/categories.json', 'r') as f:
            categories = json.load(f)

class CreateReviewForm(forms.Form):
    product_name = forms.CharField(label="Nombre del Producto", required=True, widget=forms.TextInput(attrs={'placeholder':'Nombre del Producto', 'class': 'form-control'}))
    content = forms.CharField(label='Haz tu reseña...', widget=forms.Textarea(attrs={'placeholder':'Haz tu reseña...', 'class': 'form-control h-50'}), max_length=500)
    category = forms.ChoiceField(label='Select a country', widget=forms.Select(attrs={'class': 'form-select text-muted'}), choices=[(category['id'], category['name']) for category in categories],  required=True)
    PUNCTUATIONS=[
       ("1", "ONE_STAR"),
       ("2", "TWO_STARS"),
       ("3", "THREE_STARS"),
       ("4", "FOUR_STARS"),
       ("5", "FIVE_STARS"),
    ]
    punctuation = forms.ChoiceField(label="Puntuacion", widget=forms.Select(attrs={'class': 'form-select text-muted'}),choices=PUNCTUATIONS)
    object_image = forms.ImageField(label="Imagen del producto...")

class FilterMyReviews(forms.Form):
        choices = [("0", "Todas las categorias")]
        choices += [(category['id'], category['name']) for category in categories]
        category = forms.ChoiceField(label='Select a country', widget=forms.Select(attrs={'class': 'form-select text-muted'}), choices=choices,  required=True)


class FilterAllReviews(forms.Form):
        username = forms.CharField(label="Autor reseña", required=False, widget=forms.TextInput(attrs={'placeholder':'Autor reseña', 'class': 'form-control'}))
        choices = [("0", "Todas las categorias")]
        choices += [(category['id'], category['name']) for category in categories]
        category = forms.ChoiceField(label='Select a country', widget=forms.Select(attrs={'class': 'form-select text-muted'}), choices=choices,  required=True)

class CreateComment(forms.Form):
        content = forms.CharField(label='Haz tu comentario...', widget=forms.Textarea(attrs={'placeholder':'Haz tu comentario...', 'class': 'form-control h-50'}), max_length=500)