
from django.forms import ModelForm, TextInput
from .models import City
from django.contrib.auth.models import User

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = [ 'first_name','last_name','email','username','password']

class CreateGoalForm(ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'user']
