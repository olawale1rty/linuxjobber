from django.shortcuts import render

# Create your views here.
import random

from django.http import HttpResponse
from .models import ScrumyGoals, GoalStatus
from django.contrib.auth.models import User

def index(request):
	output = ScrumyGoals.objects.filter(goal_name='Learn Django')
	return HttpResponse(output)

def move_goal(request, **kwargs):
	output = ScrumyGoals.objects.get(goal_id=kwargs['goal_id'])
	return HttpResponse(output) 

def add_goal(request):
	add_goal = ScrumyGoals.objects.create(goal_name = 'Keep Learning Django', goal_id = random.randint(1000, 9999), created_by = 'Louis', moved_by = 'Louis', owner = 'Louis', goal_status = GoalStatus.objects.get(status_name='Weekly Goal'), user = User.objects.get(username='louis'))
	add_goal.save()
	return HttpResponse('Saved Successfully')

def home(request):
	dictionary = {}
	# goal = ScrumyGoals.objects.all()
	# output = ', '.join([eachgoal.goal_name for eachgoal in goal])
	# return HttpResponse(output)
	goal = ScrumyGoals.objects.get(goal_name='Learn Django')
	# print(goal[3])
	dictionary['goal_name'] = goal.goal_name
	dictionary['goal_id'] = goal.goal_id
	dictionary['user'] = goal.user 
	return render(request, 'moshoodscrumy/home.html', dictionary)