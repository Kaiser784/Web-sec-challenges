
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from .models import challenges_table


class SubmitFlag(forms.Form):
	Flag = forms.CharField(label="Flag                       :")

# Create your views here.
def home(request):
	challenges = challenges_table.objects.all()

	context = {
		'challenges': challenges,
	}
	return render(request,'challenges/home.html', context)
