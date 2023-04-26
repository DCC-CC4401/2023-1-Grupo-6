from django import forms


class LogInForm(forms.Form):
    nick_name = forms.CharField(label="Nickname")
    password = forms.CharField(widget=forms.PasswordInput)