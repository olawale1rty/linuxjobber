from django.urls import path, include
from moshoodscrumy import views

urlpatterns = [
    path('', views.index),
    
]
