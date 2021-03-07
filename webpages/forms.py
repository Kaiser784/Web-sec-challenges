from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class InputForm(UserCreationForm):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
