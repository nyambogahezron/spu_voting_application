from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import User
from administration_app.models import Election, Position, RunningMate, Ballot
from .forms import UserForm, UserCreationFormCustomized
from django.db.models import Count, F, ExpressionWrapper, FloatField


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            messages.success(request, "logged in successful", extra_tags='success')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "Invalid details", extra_tags='warning')
    context = {}
    return render(request, 'base/login.html', context)


def registerUser(request):
    form = UserCreationFormCustomized()
    if request.method == 'POST':
        form = UserCreationFormCustomized(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "something went wrong!", extra_tags='warning')
    context = {'form': form}
    return render(request, 'base/register.html', context)


@login_required
def home(request):
    current_time = timezone.now()
    elections = Election.objects.filter(end_date__gt=current_time)
    data = []
    for election in elections:
        positions = Position.objects.filter(election=election)
        election_data = {
            'election': election,
            'positions': [],
        }
        for position in positions:
            # Check if the user has already voted for this position in this election
            user_has_voted = Ballot.objects.filter(user=request.user, position=position, election=election).exists()
            if not user_has_voted:
                running_mates = RunningMate.objects.filter(position=position, election=election)
                position_data = {
                    'position': position,
                    'running_mates': running_mates,
                }
                election_data['positions'].append(position_data)
        data.append(election_data)
    context = {
        'data': data,
    }
    return render(request, 'base/home.html', context)


@login_required
def vote(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        running_mate_id = request.POST.get('running_mate_id')
        election_id = request.POST.get('election_id')
        position_id = request.POST.get('position')
        # Fetch objects from database
        user = User.objects.get(id=user_id)
        running_mate = RunningMate.objects.get(id=running_mate_id)
        election = Election.objects.get(id=election_id)
        position = Position.objects.get(id=position_id)
        ballot = Ballot.objects.filter(user=user, election=election, position=position)
        # Condition to check if the voter has already voted
        if ballot.exists():
            messages.info(request, 'You have already voted for this running mate in this election.', extra_tags='info')
        else:
            Ballot.objects.create(user=user, running_mate=running_mate, election=election, position=position)
            messages.success(request, 'Your vote has been recorded.', extra_tags='success')
    return redirect('home')



@login_required
def results(request):
    elections = Election.objects.all()
    data = []

    for election in elections:
        election_data = {"name": election.name, "positions": []}

        positions = Position.objects.filter(election=election)

        for position in positions:
            position_data = {"title": position.title, "total_votes": 0, "running_mates": []}

            running_mates = RunningMate.objects.filter(position=position, election=election)

            # Calculate total votes for this position
            total_votes_in_position = Ballot.objects.filter(election=election, running_mate__position=position).count()
            position_data["total_votes"] = total_votes_in_position

            for running_mate in running_mates:
                # Calculate total votes for this running mate
                total_votes_for_running_mate = Ballot.objects.filter(running_mate=running_mate).count()
                running_mate.total_votes = total_votes_for_running_mate

                # Calculate percentage of votes for this running mate
                if total_votes_in_position > 0:
                    running_mate.percentage_votes = (total_votes_for_running_mate / total_votes_in_position) * 100
                else:
                    running_mate.percentage_votes = 0

                position_data["running_mates"].append(running_mate)

            position_data["running_mates"] = sorted(position_data["running_mates"], key=lambda rm: rm.total_votes, reverse=True)
            election_data["positions"].append(position_data)

        data.append(election_data)

    return render(request, 'base/results.html', {"elections": data})



def logoutUser(request):
    # Logs out the user
    logout(request)
    return redirect('login')
