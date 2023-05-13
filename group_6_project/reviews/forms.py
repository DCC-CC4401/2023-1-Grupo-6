from django import forms
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
    email = forms.EmailField( required=True,widget=forms.EmailInput(attrs={'placeholder':'Correo electrónico', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Contraseña', 'class': 'form-control'}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Repetir contraseña', 'class': 'form-control'}))

with open('reviews/assets/categories.json', 'r') as f:
            categories = json.load(f)

class CreateReviewForm(forms.Form):
    product_name = forms.CharField(label="Nombre del Producto", required=True, widget=forms.TextInput(attrs={'placeholder':'Nombre del Producto', 'class': 'form-control'}))
    content = forms.CharField(label='Haz tu reseña...', widget=forms.Textarea(attrs={'placeholder':'Haz tu reseña...', 'class': 'form-control'}), max_length=500)
    category = forms.ChoiceField(label='Select a country', widget=forms.Select(attrs={'class': 'form-select text-muted'}), choices=[(category['id'], category['name']) for category in categories],  required=True)
    PUNCTUATIONS=[
       (1, "ONE_STAR"),
       (2, "TWO_STARS"),
       (3, "THREE_STARS"),
       (4, "FOUR_STARS"),
       (5, "FIVE_STARS"),
    ]
    punctutation = forms.ChoiceField(label="Puntuacion", widget=forms.Select(attrs={'class': 'form-select text-muted'}),choices=PUNCTUATIONS)
    
