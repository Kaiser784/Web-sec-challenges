from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class InputForm(UserCreationForm):
    firstname = forms.CharField(max_length=25)
    lastname = forms.CharField(max_length=25)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email', 'username', 'password1', 'password2')
