from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import InputForm

# Create your views here.

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
    return render(request, 'register/login.html', {'form': form})