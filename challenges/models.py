from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class challenges_table(models.Model):
	title = models.CharField(max_length=20, unique = True)
	description = models.CharField(max_length=200)
	venari = models.PositiveIntegerField(default = 0, blank=True)
	location = models.CharField(max_length = 50)
	difficulty = models.CharField(max_length=10)
	author = models.CharField(max_length=20)
	flag = models.CharField(max_length=150)
	hints = models.CharField(max_length=200, default='', blank=True)

	users = models.ManyToManyField(User, through='ChallengeUserRelation')

	def __str__(self):
		return "{}".format(self.title)


class ChallengeUserRelation(models.Model):
	user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
	challenge = models.ForeignKey(challenges_table, to_field='title', on_delete=models.CASCADE)
	done = models.BooleanField(blank=True, default= False)