from django.contrib import admin

from .models import Election, Position, Voter, RunningMate, Ballot

admin.site.register(Election)
admin.site.register(Position)
admin.site.register(Voter)
admin.site.register(RunningMate)
admin.site.register(Ballot)
