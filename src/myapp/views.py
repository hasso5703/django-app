from django.shortcuts import render, HttpResponse
from .models import TodoItem
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def todos(request):
    return render(request, 'todos.html', {"todos": TodoItem.objects.all()})