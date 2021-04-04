from django import forms
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import ChallengeUserRelation, challenges_table, LeaderBoard

# Create your views here.
def home(request):
	record1 = challenges_table.objects.all()

	if request.user.is_authenticated:
		current_user = request.user
		record2 = LeaderBoard.objects.get(user = current_user)
		record3 = ChallengeUserRelation.objects.filter(user = current_user)

		query_set = ChallengeUserRelation.objects.select_related('challenge').filter(user = current_user)

		context = {
			'challenges': record1,
			'challenges_modal': query_set,
			'leaderboard': record2,
		}
		
		var = request.POST
		flagcheck = var.get("flag_check", False)
		titlecheck = var.get("title_check", False)
		if flagcheck:
			record1 = challenges_table.objects.get(title = titlecheck)
			if record1.flag == flagcheck:
				print("YES")
				record2.venari = record2.venari + record1.venari
				record2.solves = record2.solves + 1
				record2.save()
				for record in record3:
					if str(record.challenge) == str(titlecheck):
						record.done = True
						record.save()
			else:
				print("NO")
			return HttpResponseRedirect(reverse('webpages-home'))

		return render(request,'challenges/home.html', context)

	else:
		context = {
			'challenges': record1,
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