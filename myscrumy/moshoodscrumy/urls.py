from django.urls import path, include
from moshoodscrumy import views

urlpatterns = [
    path('movegoal/<int:goal_id>', views.move_goal),
    path('', views.index),
    path('addgoal/', views.add_goal),
    path('home/', views.home, name='about'),
    path('accounts/', include('django.contrib.auth.urls')), # Lab16 Task One
]
