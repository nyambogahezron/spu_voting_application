from django.shortcuts import render
from django.http import JsonResponse
from .models import Ballot, RunningMate, Election


def check_ballot(request, running_mate_id, election_id):
    user = request.user
    try:
        running_mate = RunningMate.objects.get(id=running_mate_id)
        election = Election.objects.get(id=election_id)
    except (RunningMate.DoesNotExist, Election.DoesNotExist):
        return JsonResponse({'error': 'RunningMate or Election does not exist'}, status=404)
    ballot_exists = Ballot.objects.filter(user=user, running_mate=running_mate, election=election).exists()
    return JsonResponse({'ballot_exists': ballot_exists})
