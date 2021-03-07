from django.contrib import admin
from .models import challenges_table, ChallengeUserRelation

# Register your models here.

admin.site.register(challenges_table)
admin.site.register(ChallengeUserRelation)