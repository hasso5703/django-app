from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.home, name='app_home'),
    path('todos/', views.todos, name='app_todos'),
]