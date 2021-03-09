from django.contrib import admin
from .models import challenges_table, ChallengeUserRelation, LeaderBoard

# Register your models here.

admin.site.register(challenges_table)
admin.site.register(ChallengeUserRelation)
admin.site.register(LeaderBoard)