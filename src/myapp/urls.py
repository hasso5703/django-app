from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.home),
    path('todos/', views.todos),
]