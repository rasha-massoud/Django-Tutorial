from django.urls import path
from . import views 

urlpatterns = [
    path('', views.basicIndex, name='basicIndex'),
    path('resume', views.onlineTemplate, name='onlineTemplate'),
    path('wordCounter', views.wordCounter, name='wordCounter'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),

]