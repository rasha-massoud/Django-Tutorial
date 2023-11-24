from django.urls import path
from . import views 

urlpatterns = [
    path('basic', views.basicIndex, name='basicIndex'),
    path('online', views.onlineTemplate, name='onlineTemplate'),
    path('wordCounter', views.wordCounter, name='wordCounter'),
    path('counter', views.counter, name='counter'),
]