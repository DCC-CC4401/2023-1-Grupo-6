from django import forms


class LogInForm(forms.Form):
    nick_name = forms.CharField(label="Nickname")
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    # name = forms.CharField(label="Nombre", required=True,)
    # last_name = forms.CharField(label="Apellido", required=True,)
    # country = forms.ModelChoiceField(queryset=Country.objects.all(), required=True,)
    # birth_date = forms.DateTimeField(required=True,)
    nick_name = forms.CharField(label="Nombre de usuario", required=True,widget=forms.TextInput(attrs={'placeholder':'Nick_name','style': 'width: 300px; background-color: rgba(3,138,255,1)', 'class': 'form-control'}))
    email = forms.EmailField( required=True,widget=forms.EmailInput(attrs={'placeholder':'Email','style': 'width: 300px; background-color: rgba(3,138,255,1)', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(),)
    apodo = forms.CharField(label="Apodo", required=True,)
    # repeat_password = forms.CharField(widget=forms.PasswordInput())

class CreateReviewForm(forms.Form):
    CATEGORIES=(
        ('1', 'Comida'),
        ('2','Hoteles'),
        ('3','Computadores'),
    )
    
    review_title=forms.CharField(label="Nombre del producto", max_length=50)
    main_text=forms.CharField(label="Contenido de la reseña",max_length=300)
    category=forms.ChoiceField(choices=CATEGORIES)
    #punctuation=
