
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
#from .models import challenges

class SubmitFlag(forms.Form):
	Flag = forms.CharField(label="Flag                       :")

# Create your views here.
'''
def home(request):
	return render(request,'challenges/home.html',{
		"form":SubmitFlag(), "challenges":challenges.objects.all().first()
		})

'''
def home(request):
	return render(request,'challenges/home.html',{
		"form":SubmitFlag()
		})

'''
def inspect(request):
	return render(request,'challenges/inspect.html')
'''
def robots(request):
	return render(request,'challenges/robots.html')
'''
def read_file(request):
	f = open("robots.txt",'r')
	content = f.read()
	f.close()
	return HttpResponse(content,content_type="text/plain")
'''
    
def warmup(request):
	return render(request,'challenges/warmup.html')