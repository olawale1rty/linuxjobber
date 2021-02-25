from django.urls import path
from . import views
from django.urls import include, path

urlpatterns = [
	path('test/', views.test, name='test'),
	path('connect/', views.connect, name='connect'),
	path('disconnect/', views.disconnect, name='disconnect')
]