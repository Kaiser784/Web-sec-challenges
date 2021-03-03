from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import InputForm
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
            messages.success(request, f'Your account has been created!')
            return render(request, 'register/success.html', {'data': username})
        else:
            print(form.errors)
    else:
        form = InputForm()
    return render(request, 'register/register.html', {'form': form})

def success(request):
    return render(request, 'register/success.html')
