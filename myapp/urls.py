from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('wordCounter', views.wordCounter, name='wordCounter'),
    path('counter', views.counter, name='counter'),
]