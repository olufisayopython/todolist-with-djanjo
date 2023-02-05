from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class meta:
        model = UserCreationForm
        field = ["username", "Email", "Password1", "Password2"]