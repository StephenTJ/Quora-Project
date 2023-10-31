from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input','style':'width:500px'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input','style':'width:500px'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input','style':'width:500px'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input','style':'width:500px'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input','style':'width:500px'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input','style':'width:500px'}))
    class Meta:
        model = User 
        fields = ['username', 'password']