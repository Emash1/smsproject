from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home, name='myhome'),
    path('about/', views.about, name='myabout'),
    path('register/', views.register, name='myregister')
]