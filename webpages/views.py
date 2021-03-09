from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from .forms import InputForm
from challenges.models import ChallengeUserRelation, challenges_table, LeaderBoard
from django.contrib.auth.models import User as u

# Create your views here.

def home(request):
    return render(request, 'register/success.html')

def user_relation(user):
    user_obj = u.objects.get(username=user)

    for obj in challenges_table.objects.all():
        c = ChallengeUserRelation(user=user_obj, challenge=obj)
        c.save()

    l = LeaderBoard(user=user_obj)
    l.save()

def user_relation_when_new_challenge(ch_title):
    ch_obj = challenges_table.objects.get(title=ch_title)

    for obj in u.objects.all():
        c = ChallengeUserRelation(user=obj, challenge=ch_obj)
        c.save()


def register(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        print(request.POST, form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user_relation(username)
            messages.success(request, f'Your account has been created!')
            return redirect(reverse('login'))            
        else:
            print(form.errors)
    else:
        form = InputForm()
    return render(request, 'register/register.html', {'form': form})


def success(request):
    return render(request, 'register/success.html')
