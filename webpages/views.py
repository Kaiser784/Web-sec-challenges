from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import InputForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'register/success.html')

def register(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        print(request.POST, form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return render(request, 'register/success.html', {'data': username})
        else:
            print(form.errors)
    else:
        form = InputForm()
    return render(request, 'register/register.html', {'form': form})



































# def login_func(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             print(request.POST)
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             print(username, password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are logged in as {username}")
#                 return render(request, 'register/success.html', {'data': username})
#             else:
#                 messages.error(request, "Invalid username or password")
#         else:

#             messages.error(request, "Invalid username or password")
#     else:
#         form = AuthenticationForm()
#     return render(request, 'register/login.html', {'form': form})

# def logout_func(request):
# need to make a login function