from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_view),
    path('content/', views.content, name='content'),  # Route pour la page content
    path('system/', views.system, name='system'),  # Route pour la page system
]