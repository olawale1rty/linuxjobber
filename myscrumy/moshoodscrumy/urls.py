from django.urls import path, include
from moshoodscrumy import views

app_name = 'moshoodscrumy'
urlpatterns = [
    path('movegoal/<int:goal_id>', views.move_goal, name='movegoal'),
    path('', views.index),
    path('addgoal/', views.add_goal, name='addgoal'),
    path('home/', views.home, name='about'),
    path('accounts/', include('django.contrib.auth.urls')), # Lab16 Task One
]

