from django.db import models

# Create your models here.
'''
class challenges(models.Model):
	challenge = models.CharField(max_length=20)
	description = models.CharField(max_length=200)
	points = models.IntegerField()
	location = models.CharField(max_length = 50)
	Difficulty = models.CharField(max_length=10)
	Author = models.CharField(max_length=20)

	def __str__(self):
		return "{}".format(self.challenge)

'''