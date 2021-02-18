from django.shortcuts import render

# Create your views here.
import random

from django.http import HttpResponse
from .models import ScrumyGoals, GoalStatus
from django.contrib.auth.models import User
from django.contrib.auth.models import Group 
from .forms import SignupForm, CreateGoalForm

def index(request):
	form = SignupForm() 
	if request.method == 'POST': 
		form = SignupForm(request.POST)
		form.save()
		user = User.objects.get(username=request.POST['username'])
		my_group = Group.objects.get(name = 'Developer') 
		my_group.user_set.add(user)
		if user.groups.filter(name='Developer').exists() :
			return render(request, 'moshoodscrumy/success.html') 
	else: 
		form = SignupForm()
	return render(request, 'moshoodscrumy/index.html', {'form':form}) 

def move_goal(request, **kwargs):
	# output = ScrumyGoals.objects.get(goal_id=kwargs['goal_id'])
	# return HttpResponse(output)
	dictionary = {'error': 'A record with that goal id does not exist'}
	## LAB 14
	try: 
		obj = ScrumyGoals.objects.get(goal_id=kwargs['goal_id'])
	except Exception as e: 
		return render(request, 'moshoodscrumy/exception.html', dictionary) 
	else: 
		return HttpResponse(obj.goal_name) 

def add_goal(request):
	# add_goal = ScrumyGoals.objects.create(goal_name = 'Keep Learning Django', goal_id = random.randrange(1000, 9999, 2), created_by = 'Louis', moved_by = 'Louis', owner = 'Louis', goal_status = GoalStatus.objects.get(status_name='Weekly Goal'), user = User.objects.get(username='louis'))
	# add_goal.save()
	# return HttpResponse('Saved Successfully')
	form = CreateGoalForm() 
	if request.method == 'POST': 
		form = CreateGoalForm(request.POST)
		good_to_go = form.save(commit=False) 
		good_to_go.goal_id = random.randrange(1000, 9999, 2)
		good_to_go.created_by = 'Louis'
		good_to_go.moved_by = 'Louis'
		good_to_go.owner = 'Louis' 
		good_to_go.goal_status = GoalStatus(status_name='Weekly Goal')
		good_to_go.goal_status.save()
		good_to_go.save()
		# user = User.objects.get(username=request.user)
		# my_group = Group.objects.get(name = 'Developer') 
		# my_group.user_set.add(user)
		# if user.groups.filter(name='Developer').exists() :
		# 	return render(request, 'moshoodscrumy/success.html') 
	else: 
		form = CreateGoalForm()

	return render(request, 'moshoodscrumy/goal.html', {'form':form}) 

def home(request):
	# ## LAB 12
	# # goal = ScrumyGoals.objects.all()
	# goal = ScrumyGoals.objects.get(goal_name='Keep Learning Django')
	# # output = ', '.join([eachgoal.goal_name for eachgoal in goal])
	# # return HttpResponse(output)
	# return HttpResponse(goal)

	## LAB 13
	# dictionary = {}
	# goal = ScrumyGoals.objects.get(goal_name='Learn Django')
	# dictionary['goal_name'] = goal.goal_name
	# dictionary['goal_id'] = goal.goal_id
	# dictionary['user'] = goal.user 
	# return render(request, 'moshoodscrumy/home.html', dictionary)

	## LAB 15
	# dictionary = {}
	# users = User.objects.all()
	# weekly_goals = ScrumyGoals.objects.filter(goal_status=GoalStatus.objects.get(status_name='Weekly Goal'))
	# daily_goals = ScrumyGoals.objects.filter(goal_status=GoalStatus.objects.get(status_name='Daily Goal'))
	# verify_goals = ScrumyGoals.objects.filter(goal_status=GoalStatus.objects.get(status_name='Verify Goal'))
	# done_goals = ScrumyGoals.objects.filter(goal_status=GoalStatus.objects.get(status_name='Done Goal'))
	# dictionary['weekly_goals'] = '  '.join([eachgoal_1.goal_name for eachgoal_1 in weekly_goals])
	# dictionary['daily_goals'] = '  '.join([eachgoal_1.goal_name for eachgoal_1 in daily_goals])
	# dictionary['verify_goals'] = '  '.join([eachgoal_1.goal_name for eachgoal_1 in verify_goals])
	# dictionary['done_goals'] = '  '.join([eachgoal_1.goal_name for eachgoal_1 in done_goals])
	# dictionary['users'] = users 
	# dictionary['user_real'] = '  '.join([eachgoal_1.username for eachgoal_1 in users])
	# return render(request, 'moshoodscrumy/home.html', dictionary)

	##Lab18
	return render(request, 'moshoodscrumy/home.html')	

