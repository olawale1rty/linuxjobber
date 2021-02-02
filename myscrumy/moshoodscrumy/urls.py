from django.urls import path, include
from moshoodscrumy import views

urlpatterns = [
    path('movegoal/<int:goal_id>', views.move_goal),
    path('', views.index),
    
]
