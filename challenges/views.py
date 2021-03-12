from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import challenges_table, LeaderBoard


class SubmitFlag(forms.Form):
	Flag = forms.CharField(label="Flag                       :")

# Create your views here.
def home(request):
	challenges = challenges_table.objects.all()

	context = {
		'challenges': challenges,
	}
	return render(request,'challenges/home.html', context)

def leaderboard(request):
	context = {}
	if not request.user.is_authenticated:
		context['everyone'] = LeaderBoard.objects.all().order_by('-venari', 'last_solved')
	else:
		current_user = request.user
		obj = LeaderBoard.objects.get(user = current_user)
		points = obj.venari
		user_time = obj.last_solved
		
		context['before'] = LeaderBoard.objects.filter(
			Q(venari__gt = points) | Q(venari = points, last_solved__lt = user_time)
		).order_by('-venari', 'last_solved')
		context['now'] = obj
		context['after'] = LeaderBoard.objects.filter(
			Q(venari__lt = points) | Q(venari = points, last_solved__gt = user_time)
		).order_by('-venari', 'last_solved')

	return render(request, 'leaderboard/leaderboard.html', {'context': context})